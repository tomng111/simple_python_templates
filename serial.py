import serial
import time

daten = serial.Serial('COM3', 9600)
time.sleep(1)

while True:
    sendData = input("Enter the command: ")
    sendData = sendData + '\r'
    daten.write(sendData.encode())
