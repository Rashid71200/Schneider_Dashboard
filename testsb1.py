import mysql.connector
import random
import time
import re


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
    
basket = [
        'POWER_METER_4'
]

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

def create_table(connection, table_name, fruits_list):
    try:
        cursor = connection.cursor()
        column_definitions = ', '.join([re.sub('[^A-Za-z0-9]+', '', col_name) for col_name in fruits_list])
        create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY, `{column_definitions}`)"
        #print(create_table_query)
        cursor.execute(create_table_query)
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print(f"Error creating table {table_name}:", err)

def insert_data(connection, table_name, data):
    try:
        cursor = connection.cursor()
        column_names = ', '.join(data.keys())
        column_values = ', '.join([str(random.randint(1, 9)) for value in data.values()])
  
        cursor.execute(f"INSERT INTO `{table_name}` ({column_names}) VALUES ({column_values})")
        connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print("Error inserting data:", err)

if __name__ == "__main__":
    connection = create_connection()
    db_name = "power_meter"
    table_name = basket
    create_database(connection, db_name)
    #create_table(connection, table_name)

    while True:
        for i in range(len(basket)):
            table_name = basket[i]
            create_table(connection, table_name, fruts_list)
            print(table_name)               
            insert_data(connection, table_name, fruts_list)
            time.sleep(1)   

