import serial

# Seri portu aç
serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
#serial_port2 = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

def read_serialport_and_publish():
    # Seri portta veri varsa oku
    usb_data = serial_port.readline().decode('utf-8').strip()
    sag,sol = usb_data_splitter(usb_data)
    linear_actuator =0
    if sol ==1 and sag==0:
        right_wheel_velocity = 300
        left_wheel_velocity = 150
    if sag ==1 and sol ==0:
        right_wheel_velocity = 150
        left_wheel_velocity = 300
    if sag == 0 and sol ==0: 
        right_wheel_velocity = 300
        left_wheel_velocity = 300

    right_wheel_velocity_str = f'{int(right_wheel_velocity):05}'
    left_wheel_velocity_str = f'{int(left_wheel_velocity):05}'
    linear_actuator_str = f'{int(linear_actuator):05}'
    print("right_wheel_velocity_str:",right_wheel_velocity_str)
    print("left_wheel_velocity_str: ",left_wheel_velocity_str)

    #command = f'{right_wheel_velocity_str},{left_wheel_velocity_str},{linear_actuator_str}\n'
    #serial_port2.write(command.encode())

def usb_data_splitter(usb_data):
    # Veriyi "Sensor 1: 0 | Sensor 2: 0" formatında ayrıştır
    parts = usb_data.split('|')
    sol = float(parts[0].split(':')[1].strip())
    sag = float(parts[1].split(':')[1].strip())
    print("sol:", sol)
    print("sag:", sag)
    return sol, sag

# Ana döngü
while True:
    read_serialport_and_publish()
