import serial
import time

daten = serial.Serial('COM3', 9600)

time.sleep(1)

while True:
    while daten.inWaiting() == 0:
        pass
    # Received data processing
    recData = daten.readline()
    recData = str(recData, 'utf-8')
    recData = recData.strip('\r\n')
    # print(recData)
    splData = recData.split(',')
    print(splData)
    # Changing to float
    x = float(splData[0])
    y = float(splData[1])
    z = float(splData[2])
    print('x = ', x, ' - y = ', y, ' - z = ', z)
