import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/cu.usbmodem1421'
ser.open()
while True:
    print(ser.readline().split())
