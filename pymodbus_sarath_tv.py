from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time

#client = ModbusTcpClient( '192.63.12.155', port=63,framer=ModbusFramer)
#update xxx with IP of the IP of the RS485-Ethernet adapter and yy with port number of the RS485-Ethernet adapter

update_time = 2
port = 502


ip_list = {
              
                '127.0.0.2': 5,
                '127.0.0.3': 3,
                '127.0.0.4': 5,
                '127.0.0.5': 2,
                '127.0.0.6': 7,
                '127.0.0.7': 5,
                '127.0.0.8': 9,
       }


holding_register_list = {
"Active Energy Delivered (Into Load)": 2700,
    "Active Energy Received (Out of Load)": 2702,
    "Active Energy Delivered + Received": 2704,
    "Active Energy Delivered- Received": 2706,
    "Reactive Energy Delivered": 2708,
    "Reactive Energy Received": 2710,
    "Reactive Energy Delivered + Received": 2712,
    "Reactive Energy Delivered - Received": 2714,
    "Apparent Energy Delivered": 2716,
    "Apparent Energy Received": 2718,
    "Apparent Energy Delivered + Received": 2720,
    "Apparent Energy Delivered - Received": 2722,
    
    "Current A": 3000,
    "Current B": 3002,
    "Current C": 3004,
    "Current N": 3006,
    "Current G": 3008,
    "Current Avg": 3010,
    
    "Current Unbalance A": 3012,
    "Current Unbalance B": 3014,
    "Current Unbalance C": 3016,
    "Current Unbalance Worst": 3018,
    
    "Voltage A-B": 3020,
    "Voltage B-C": 3022,
    "Voltage C-A": 3024,
    "Voltage L-L Avg": 3026,
    "Voltage A-N": 3028,
    "Voltage B-N": 3030,
    "Voltage C-N": 3032,
    "Voltage N-G": 3034,
    "Voltage L-N Avg": 3036,
    
    "Voltage Unbalance A-B": 3038,
    "Voltage Unbalance B-C": 3040,
    "Voltage Unbalance C-A": 3042,
    "Voltage Unbalance L-L Worst": 3044,
    "Voltage Unbalance A-N": 3046,
    "Voltage Unbalance B-N": 3048,
    "Voltage Unbalance C-N": 3050,
    "Voltage Unbalance L-N Worst": 3052,
    
    "Active Power A": 3054,
    "Active Power B": 3056,
    "Active Power C": 3058,
    "Active Power Total": 3060,
    "Reactive Power A": 3062,
    "Reactive Power B": 3064,
    "Reactive Power C": 3066,
    "Reactive Power Total": 3068,
    "Apparent Power A": 3070,
    "Apparent Power B": 3072,
    "Apparent Power C": 3074,
    "Apparent Power Total": 3076,
       }

number_of_meter = len(ip_list)



def get_data(ip, port, number_of_slave, holding_register_list):

    client = ModbusTcpClient( ip, port ) #,framer=ModbusFramer)

    for name_of_register, register in holding_register_list.items():
        response = client.read_holding_registers((register-1), 2, unit=int(number_of_slave))
        print(f"For {name_of_register} Register value is : {register}")

        decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
        reading=decoder.decode_32bit_float()
        print (name_of_register + str(reading))

        if response.isError():
            print(response.isError())

        assert(not response.isError())    
        decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
        reading=decoder.decode_32bit_float()
        print (name_of_register + str(reading))
        time.sleep(0.1)
    client.close()
    time.sleep(0.1)
    


while True:
    for ip, value in ip_list.items():
        print(ip)
        
        
        for i in range(value):
            number_of_slave = int(i) + 1
            print(f"Number of slave: {number_of_slave}")
            data = get_data(ip, port, number_of_slave, holding_register_list)
            time.sleep(0.1)
        
        time.sleep(update_time)


