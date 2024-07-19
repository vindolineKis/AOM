import pyvisa as visa
import time


def open_resource(address):
    rm = visa.ResourceManager()
    instrument = rm.open_resource(address)
    return instrument

# write the current to port 1 and port 2
def set_current_qpx(instrument,current_value1,current_value2):
    # if current_value1!=None: Write current to output 1
    if current_value1!=None:
        command1 = f'V1 {current_value1}'
        instrument.write(command1)
        print(f'Current set to Port1 {current_value1} A')
    else:
        print("No current value for Port1") 
    # if current_value2!=None: Write current to output 2
    if current_value2!=None:
        command2 = f'V2 {current_value2}'
        instrument.write(command2)
        print(f'Current set to Port2 {current_value2} A')
    else:
        print("No current value for Port2")


address='ASRL6::INSTR'
qpx = open_resource(address)
print(qpx.query('*IDN?'))

# Write voltage to both outputs
set_current_qpx(qpx,16,15)

# Find out voltage at both outputs
V1=qpx.query('V1?')
V2=qpx.query('V2?')
print(V1)
print(V2)

time.sleep(1)
print("CONNECTED")
