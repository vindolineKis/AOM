
import pyvisa as visa
import time

def set_current(instrument,current_value):
    print({current_value})
    # command=":SOUR1:CURR:LEVel:IMM:AMPL {}".format(current_value)
    command=f":SOUR1:CURR:LEVel:IMM:AMPL {current_value}"
    instrument.write(command)
    print("Current set to {} A".format(current_value))

def turn_on_tec(instrument):
    command=":OUTPut2:STATe ON"
    instrument.write(command)
    print("TEC on")

def main():
    rm = visa.ResourceManager()
    instruments = rm.list_resources()
    instrument_address='USB0::0x1313::0x804F::M00939700::INSTR'
    instrument=rm.open_resource(instrument_address)
    # instrument_id=instrument.query('*IDN?')
    # print(instrument_id)
    print("Connected instruments:",instruments)
    
    # turn_on_tec(instrument)
    # time.sleep(1)
    desired_current=0.12
    set_current(instrument,desired_current)
    print(instrument.query(":SOUR1:CURR:LEVel:IMM:AMPL?"))
    instrument.close()

if __name__ == "__main__":
    main()