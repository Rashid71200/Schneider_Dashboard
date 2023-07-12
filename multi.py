from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder, Endian
##from datetime import datetime
import time
import os

variable_value = 20
valueBackup = 0

def backup_modbus(address, l ):
    global valueBackup
    client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)
    try:
        client.connect()
        result = client.read_holding_registers(address=address, count=1, unit=(l+1))
        valueBackup = result.registers[0]
    except:
        time.sleep(1)
        backup_modbus(address, l )

    print("reading from backup....................................................................................................... ")
    return valueBackup


def start_modbus(variable_value):
    b = variable_value
    l_values = []  # List to store the values from each slave
    client = ModbusSerialClient(method="rtu", port="COM5", stopbits=1, bytesize=8, parity='N', baudrate=9600)
    
    try:
        client.connect()
    except:
        time.sleep(4)
        start_modbus(variable_value)

    for l in range(b):  # Iterate over the slave addresses (1 to b)
        print(f"number of loop {l}")
        valueS = []  # List to store the key-value pairs for each slave

        update_values = {
            "voltage": 3019,
            "current": 3009,
            "frequency": 3059,
            "power": 3109
        }
        
        for key, address in update_values.items():

            # Reading Holding Registers.............................
            try:
                result = client.read_holding_registers(address=address, count=2, unit=(l+1))
                value = result.registers[0]
                decoder = BinaryPayloadDecoder.fromRegisters(response1.registers, Endian.Big, wordorder=Endian.Big)
                #print("Voltage =", decoder.decode_32bit_float(), "V")
                value =str( round(decoder.decode_32bit_float(), 2))

            except:
                time.sleep(1)
                value = backup_modbus(address, l )
            #.......................................................


        print('time to sleep')
        time.sleep(0.01)


    client.close()
    return l_values  # Return the list of dictionaries

while True:
    value = start_modbus(variable_value)
    print(value)
    time.sleep(5)
