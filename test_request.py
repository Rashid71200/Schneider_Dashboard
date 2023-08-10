import requests

#from pymodbus.client.sync import ModbusSerialClient
#from openpyxl import Workbook, load_workbook
from datetime import datetime
import time
import os
import random

variable_value = 20
valueBackup = 0

def start_modbus(variable_value):
    x = random.randint(100, 999)
    return x



def send_data_to_flask(value):
    url = 'http://localhost:5000/home'  # Replace with the Flask server URL
    data = {'value': value}
    print(data)

    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('Data sent successfully')
        else:
            print('Failed to send data')
    except requests.exceptions.RequestException as e:
        print(f'An error occurred: {e}')

while True:
    value = start_modbus(variable_value)
    send_data_to_flask(value)
    time.sleep(5)