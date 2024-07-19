import pyvisa as visa
import time

rm =visa.ResourceManager()
res = rm.list_resources()

qpx = rm.open_resource('ASRL6::INSTR')
print(qpx.query('*IDN?'))

# Write voltage to both outputs
command = f'V2 15'
command = f'V1 16'
qpx.write(command)

# Find out voltage at both outputs
V1=qpx.query('V1?')
V2=qpx.query('V2?')
print(V1)
print(V2)
 

time.sleep(1)


print(res)
print("CONNECTED")
