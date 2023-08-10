from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
import time
import mysql.connector

update_time = 2
port = 502

ip_list = {
      '127.0.0.9': 4,
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

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="$n200000G"
    )

def create_database(connection, db_name):
    try:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
    except mysql.connector.Error as err:
        print("Error creating database:", err)
        exit(1)

def create_table(connection, table_name, columns):
    try:
        cursor = connection.cursor()
        column_definitions = ', '.join([f"{col_name} FLOAT" for col_name in columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {column_definitions})")
    except mysql.connector.Error as err:
        print("Error creating table:", err)
        exit(1)

def insert_data(connection, table_name, data):
    try:
        cursor = connection.cursor()
        column_names = ', '.join(data.keys())
        column_values = ', '.join([str(value) for value in data.values()])
        cursor.execute(f"INSERT INTO {table_name} ({column_names}) VALUES ({column_values})")
        connection.commit()
    except mysql.connector.Error as err:
        print("Error inserting data:", err)

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
    return name_of_register, reading

if __name__ == "__main__":
    connection = create_connection()
    db_name = "power_meter2"
    create_database(connection, db_name)
    
    while True:
        for ip, value in ip_list.items():
            print(ip)
            data = {}
            
            for i in range(value):
                number_of_slave = int(i) + 1
                print(f"Number of slave: {number_of_slave}")
                data.update(get_data(ip, port, number_of_slave, holding_register_list))
                time.sleep(0.1)
            
            # Insert data into MySQL table
            table_name = "powermeter1"
            create_table(connection, table_name, data.keys())
            insert_data(connection, table_name, data)
            
            time.sleep(update_time)
