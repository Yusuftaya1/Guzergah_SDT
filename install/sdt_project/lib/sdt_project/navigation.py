#!/usr/bin/env python3
"""
QR BİLGİLERİ KULLANILARAK ARACIN DÜZ GİTMESİ YA DA DÖNÜŞ YAPMASI SAĞLANIR

"qr_status" KULLANILARAK ARACIN GİTMESİ GEREKEN YÖN BELİRLENİR VE BUNA GÖRE MOTOR
HIZLARI "/AGV/motor_values_node" a GÖNDERİLİR 

AYRICA "qr_status" KULLANILARAK LİFTİN ÇALIŞMASI DA "/AGV/motor_values_node" ÜZERİNDEN
KONTROL EDİLİR

"/cmd_vel" de KULLANILABİLİR

  ---mode_status --- mode_status node--- 
motor_values NEREDEN ALINACAK ONU BELİRLER

1 == line_follow
2 == turn
3 == escape_block
mode_status node

"""

