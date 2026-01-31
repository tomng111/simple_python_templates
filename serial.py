import serial
import time

daten = serial.Serial('COM3', 9600)
time.sleep(1)

#while True:
#    sendData = input("Enter the command: ")
#    sendData = sendData + '\r'
#    daten.write(sendData.encode())

def ledEin():
    daten.write('e1\r'.encode())
def ledAus():
    daten.write('a1\r'.encode())

while True:
    ledEin()
    time.sleep(2)
    ledAus()
    time.sleep(2)
