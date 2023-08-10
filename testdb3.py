import mysql.connector
import random
import time
import re

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer
from datetime import datetime


fruts_list = {
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
    
basket = {
        'POWER_METER_4': '127.0.0.2',
       
}

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="$n200000G"
    )


def get_data(register, ip, port, max_retries=3):
    """
    Read data from a Modbus register.

    Args:
        register (int): The Modbus register address.
        ip (str): The IP address of the Modbus device.
        port (int): The port number for Modbus communication.
        max_retries (int): Maximum number of retries in case of error.

    Returns:
        str: The reading from the Modbus register as a string.
    """
    retries = 0
    while retries < max_retries:
        try:
            client = ModbusTcpClient(ip, port)
            response = client.read_holding_registers((register - 1), 2, unit=1)
            decoder = BinaryPayloadDecoder.fromRegisters(response.registers, Endian.Big, wordorder=Endian.Little)
            reading = decoder.decode_32bit_float()
            client.close()
            return str(reading)
        except Exception as e:
            print("Error reading data:", e)
            retries += 1
            print(f"Retrying ({retries}/{max_retries})...")
            time.sleep(1)  # Add a delay before retrying
    return "Error: Max retries reached"

# Usage example:


def insert_data(connection, table_name, data, basket):
    """Insert data into the specified MySQL table."""
    try:
        ip = basket[table_name]
        cursor = connection.cursor()

        # Get current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Use the specified database
        cursor.execute(f"USE power_meter")

        # Column names and values, including timestamp
        column_names = ', '.join([f"`{col}`" for col in data.keys()] + ["`timestamp`"])
        column_values = ', '.join([get_data(value, ip, 502) for value in data.values()] + ["'" + timestamp + "'"])  # Corrected timestamp format
        
        # Construct the INSERT query
        insert_query = f"INSERT INTO `{table_name}` ({column_names}) VALUES ({column_values})"
        
        # Execute the query and commit changes
        cursor.execute(insert_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print("Error inserting data:", err)


if __name__ == "__main__":
    connection = create_connection()
    db_name = "power_meter"
    table_name = []
    

    for table_name1 in basket.keys():
        table_name.append(table_name1)

    print(table_name)
    

    while True:
        for table in table_name:
            print(f"the range of table_list: {table}")
            table_name1 = table
            #create_table(connection, table_name, fruts_list)
            print(f'the name of table_list: {table_name1}')               
            insert_data(connection, table_name1, fruts_list, basket)
            time.sleep(0.1)   