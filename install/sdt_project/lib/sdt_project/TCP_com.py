#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json
import time

class TCP_Socket:
    def __init__(self):
        self.target_host = "10.7.91.190"
        self.target_port = 2626
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False

    def connect(self):
        try:
            self.client.connect((self.target_host, self.target_port))
            self.connected = True
        except ConnectionRefusedError:
            print("Bağlantı hatası: Sunucuya bağlanılamadı.")

    def data_transfer(self, msg):
        if not self.connected:
            self.connect()

        if self.connected:
            try:
                self.client.send(msg)  # Encode the message to bytes
                response = self.client.recv(4096)  # Receive the response from the server
                print("\nRESPONSE:" + response.decode('utf-8') + "\n")
            except ConnectionError:
                print("Bağlantı hatası: Veri gönderilirken bir hata oluştu.")

    def close(self):
        if self.connected:
            self.client.close()
            self.connected = False

def send_sensor(socket):
    msg_dict = {
        "sag_motor_sicaklik": 24.4,
        "sol_motor_sicaklik": 25.5,
        "lift_sicaklik":      26.6,
        "sag_motor_akim":     17.0,
        "sol_motor_akim":     18.0,
        "lift_akim":          5.0,
        "asiri_agirlik":      False
    }
    msg_json = json.dumps(msg_dict)
    socket.data_transfer(msg_json.encode('utf-8'))
    print(f"Sent sensor data: {msg_dict}")

def main():
    tcp_socket = TCP_Socket()
    try:
        while True:
            send_sensor(tcp_socket)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        tcp_socket.close()

if __name__ == '__main__':
    main()
