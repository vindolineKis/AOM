import serial

s = serial.Serial('COM6')
res = s.read()
print(res)