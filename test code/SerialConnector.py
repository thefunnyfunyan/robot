import serial, time

arduino = serial.Serial('COM3', 115200, timeout=.1)
#while True:
#    data = arduino.readline()
#    if data:
#        print(data.decode("utf-8"))

time.sleep(1)
arduino.write("Hello from python".encode())
while True:
    thing = input()
    arduino.write(thing.encode())
    data = arduino.readline()
    if data:
        print(data.decode())