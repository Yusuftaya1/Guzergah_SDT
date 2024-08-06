
import cv2
import numpy as np
import serial
import time

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
    data = f"{int(left_motor):05d},{int(right_motor):05d},0000"
    ser.write(data.encode())
    print(f"Motor Verisi Gönderildi: {data.strip()}")

def initialize_serial(port):
    try:
        ser = serial.Serial(port, 115200, timeout=1)
        time.sleep(2)
        return ser
    except serial.SerialException as e:
        print(f"Seri port açılırken bir hata oluştu: {e}")
        return None

def main():
    cam_index = 0 # USB kamera için uygun cihaz dizinini kullanın
    cap = cv2.VideoCapture(cam_index)

    if not cap.isOpened():
        print("Kamera açılamadı!")
        return

    cv2.namedWindow('Filtrelenmiş Görüntü', cv2.WINDOW_NORMAL)

    pid = PID(kp=1.0, ki=0.01, kd=0.1, setpoint=320)
    base_speed = 300
    max_speed = 1000

    ser_motor = initialize_serial('/dev/ttyUSB0')
    if ser_motor is None:
        print("Motor kontrolü için seri port açılamadı!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kare alınamadı!")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        threshold = 50
        _, binary = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY_INV)

        M = cv2.moments(binary)
        if M['m00'] != 0:
            cX = int(M['m10'] / M['m00'])
        else:
            cX = frame.shape[1] // 2

        control_signal = np.clip(pid.update(cX), -max_speed, max_speed)
        right_motor = np.clip(base_speed - control_signal, 0, max_speed)
        left_motor = np.clip(base_speed + control_signal, 0, max_speed)

        print(f"PID Kontrol Sinyali: {control_signal:.2f}")
        print(f"Sağ Motor: {right_motor:.2f}, Sol Motor: {left_motor:.2f}")
        send_motor_data(ser_motor, right_motor, left_motor)

        cv2.imshow('Filtrelenmiş Görüntü', binary)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    ser_motor.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

