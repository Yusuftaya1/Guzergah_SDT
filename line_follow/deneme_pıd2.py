import cv2
import numpy as np
import serial
import time
from ultralytics import YOLO


# PID Kontrolcü sınıfı
class PID:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.prev_error = 0

    def update(self, measurement):
        error = self.setpoint - measurement
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def send_motor_data(ser, right_motor, left_motor):
    try:
        data = f"{int(left_motor):05d},{int(right_motor):05d},0000"
        ser.write(data.encode())
        print(f"Motor Verisi Gönderildi: {data.strip()}")
    except Exception as e:
        print(f"Motor verisi gönderilirken bir hata oluştu: {e}")


def initialize_serial(port):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        time.sleep(2)
        return ser
    except serial.SerialException as e:
        print(f"Seri port açılırken bir hata oluştu: {e}")
        return None


def is_corner_detected(segment, frame_width):
    x1, y1, x2, y2 = map(int, segment[:4])
    width = x2 - x1
    return width > frame_width * 0.7


def calculate_center_of_mass(segments):
    total_weight = 0
    weighted_sum = 0
    for segment in segments:
        x1, _, x2, _ = map(int, segment[:4])
        width = x2 - x1
        cX = (x1 + x2) / 2
        total_weight += width
        weighted_sum += cX * width
    return weighted_sum / total_weight if total_weight > 0 else None


def main():
    cam_index = 0
    cap = cv2.VideoCapture(cam_index)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    cv2.namedWindow('YOLOv8 Segmentation', cv2.WINDOW_NORMAL)

    pid = PID(kp=0.6, ki=0.01, kd=0.4, setpoint=360)
    base_speed = 300
    max_speed = 1000

    ser_motor = initialize_serial('COM5')
    if ser_motor is None:
        print("Motor kontrolü için seri port açılamadı!")
        return

    model = YOLO('C:/Users/devri/5.pt')
    confidence_threshold = 0.05

    previous_direction = 0  # 1 for right, -1 for left
    corner_detected_time = None
    lost_line_time = None
    lost_line_timeout = 1.5  # seconds to keep moving in last direction when line is lost
    last_valid_cX = None  # Son geçerli cX değeri

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı!")
            continue

        frame_width = frame.shape[1]

        # YOLOv8 modelinden sonuçları asenkron olarak al
        results = model(frame)
        filtered_results = [result for result in results[0].boxes.data if result[4] > confidence_threshold]

        # Görüntü donmasını önlemek için segmentasyon çıktısını işlemeden önce motor verilerini gönder
        right_motor = base_speed
        left_motor = base_speed
        control_signal = 0  # Initialize control_signal to a default value

        if filtered_results:
            cX = calculate_center_of_mass(filtered_results)
            if cX is not None:
                last_valid_cX = cX  # Son geçerli cX değerini kaydet

                if is_corner_detected(filtered_results[0], frame_width):
                    if corner_detected_time is None or (time.time() - corner_detected_time) > 2:
                        corner_detected_time = time.time()
                        if cX < frame_width / 2:  # Sol köşe
                            right_motor = 100
                            left_motor = 500
                            previous_direction = -1  # Sol yön
                        else:  # Sağ köşe
                            right_motor = 500
                            left_motor = 100
                            previous_direction = 1  # Sağ yön
                    else:
                        elapsed_time = time.time() - corner_detected_time
                        if elapsed_time <= 2:
                            if cX < frame_width / 2:  # Sol köşe
                                right_motor = 100
                                left_motor = 500
                                previous_direction = -1  # Sol yön
                            else:  # Sağ köşe
                                right_motor = 500
                                left_motor = 100
                                previous_direction = 1  # Sağ yön
                        else:
                            corner_detected_time = None
                            continue
                else:
                    current_base_speed = base_speed - 50  # Hız dönüşlerde azalıyor
                    control_signal = np.clip(pid.update(cX), -max_speed, max_speed)
                    right_motor = np.clip(current_base_speed - control_signal, 0, max_speed)
                    left_motor = np.clip(current_base_speed + control_signal, 0, max_speed)

                lost_line_time = None  # Reset lost line timer
                send_motor_data(ser_motor, right_motor, left_motor)
                print(f"PID Kontrol Sinyali: {control_signal:.2f}")
                print(f"Sağ Motor: {right_motor:.2f}, Sol Motor: {left_motor:.2f}")

        else:
            if lost_line_time is None:
                lost_line_time = time.time()

            elapsed_since_lost = time.time() - lost_line_time

            if elapsed_since_lost <= lost_line_timeout and last_valid_cX is not None:
                # Son geçerli cX değerine göre manevra yap
                control_signal = np.clip(pid.update(last_valid_cX), -max_speed, max_speed)
                right_motor = np.clip(base_speed - control_signal, 0, max_speed)
                left_motor = np.clip(base_speed + control_signal, 0, max_speed)
                print(f"Çizgi kayboldu, son bilinen yöne doğru manevra yapılıyor.")
            else:
                # Çizgi uzun süre kaybolduysa en son bilinen yöne göre daha keskin manevra yap
                if last_valid_cX is not None:
                    control_signal = np.clip(pid.update(last_valid_cX), -max_speed * 1.5, max_speed * 1.5)
                    right_motor = np.clip(base_speed - control_signal, 0, max_speed)
                    left_motor = np.clip(base_speed + control_signal, 0, max_speed)
                    print("Çizgi uzun süre kayboldu, keskin manevra yapılıyor.")
                else:
                    right_motor = base_speed
                    left_motor = base_speed
                    print("Çizgi kayboldu, durduruluyor.")

            send_motor_data(ser_motor, right_motor, left_motor)

        # Segmentasyon görüntüsünü işle ve göster
        annotated_frame = results[0].plot()
        cv2.imshow('YOLOv8 Segmentation', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if ser_motor is not None:
        ser_motor.close()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
