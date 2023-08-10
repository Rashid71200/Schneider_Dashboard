from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
import time

#client = ModbusTcpClient( '192.63.12.155', port=63,framer=ModbusFramer)
#update xxx with IP of the IP of the RS485-Ethernet adapter and yy with port number of the RS485-Ethernet adapter

update_time = 2
port = 63


ip_list = {
                '127.0.0.1': 4,
                '192.63.12.156': 5,
                '192.63.12.157': 3,
                '192.63.12.158': 5,
                '192.63.12.159': 2,
                '192.63.12.160': 7,
                '192.63.12.161': 5,
                '192.63.12.162': 9,
       }

holding_register_list = {
                'volt': 4,
                'amps': 7,
                'watt': 5,
                'kilo_watt': 3,
                'kilo_watt_apm': 5,
                'power_factor': 2,
                'frequency': 5,
       }

number_of_meter = len(ip_list)



def get_data(ip, port, number_of_slave, holding_register_list):

    client = ModbusTcpClient( ip, port,framer=ModbusFramer)
        
    for name_of_register, register in holding_register_list.items():
        print(f"For {name_of_register} Register value is : {register}")
        
    

    #response = client.read_holding_registers(3926, 2, unit=int(number_of_slave))
    print(number_of_slave)
    
 
    time.sleep(1)


while True:
    for ip, value in ip_list.items():
        print(ip)
        
        
        for i in range(value):
            number_of_slave = int(i) + 1
            print(f"Number of slave: {number_of_slave}")
            data = get_data(ip, port, number_of_slave, holding_register_list)
            time.sleep(0.1)
        
        time.sleep(update_time)
