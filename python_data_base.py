import mysql.connector

# Replace these values with your actual MySQL server configuration
host = 'localhost'
user = 'root'
password = '$n200000G'
database = 'power_meter'



# Establish a connection to the MySQL server
connection = mysql.connector.connect (
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# SQL query to create the table
create_table_query = '''
CREATE TABLE `POWER_METER_4` (
    
    `timestamp` DATETIME,
    `Active Energy Delivered (Into Load)` FLOAT,
    `Active Energy Received (Out of Load)` FLOAT,
    `Active Energy Delivered + Received` FLOAT,
    `Active Energy Delivered- Received` FLOAT,
    `Reactive Energy Delivered` FLOAT,
    `Reactive Energy Received` FLOAT,
    `Reactive Energy Delivered + Received` FLOAT,
    `Reactive Energy Delivered - Received` FLOAT,
    `Apparent Energy Delivered` FLOAT,
    `Apparent Energy Received` FLOAT,
    `Apparent Energy Delivered + Received` FLOAT,
    `Apparent Energy Delivered - Received` FLOAT,
    `Current A` FLOAT,
    `Current B` FLOAT,
    `Current C` FLOAT,
    `Current N` FLOAT,
    `Current G` FLOAT,
    `Current Avg` FLOAT,
    `Current Unbalance A` FLOAT,
    `Current Unbalance B` FLOAT,
    `Current Unbalance C` FLOAT,
    `Current Unbalance Worst` FLOAT,
    `Voltage A-B` FLOAT,
    `Voltage B-C` FLOAT,
    `Voltage C-A` FLOAT,
    `Voltage L-L Avg` FLOAT,
    `Voltage A-N` FLOAT,
    `Voltage B-N` FLOAT,
    `Voltage C-N` FLOAT,
    `Voltage N-G` FLOAT,
    `Voltage L-N Avg` FLOAT,
    `Voltage Unbalance A-B` FLOAT,
    `Voltage Unbalance B-C` FLOAT,
    `Voltage Unbalance C-A` FLOAT,
    `Voltage Unbalance L-L Worst` FLOAT,
    `Voltage Unbalance A-N` FLOAT,
    `Voltage Unbalance B-N` FLOAT,
    `Voltage Unbalance C-N` FLOAT,
    `Voltage Unbalance L-N Worst` FLOAT,
    `Active Power A` FLOAT,
    `Active Power B` FLOAT,
    `Active Power C` FLOAT,
    `Active Power Total` FLOAT,
    `Reactive Power A` FLOAT,
    `Reactive Power B` FLOAT,
    `Reactive Power C` FLOAT,
    `Reactive Power Total` FLOAT,
    `Apparent Power A` FLOAT,
    `Apparent Power B` FLOAT,
    `Apparent Power C` FLOAT,
    `Apparent Power Total` FLOAT,
    `Power Factor A` VARCHAR(10),
    `Power Factor B` VARCHAR(10),
    `Power Factor C` VARCHAR(10),
    `Power Factor Total` VARCHAR(10),
    `Displacement Power Factor A` VARCHAR(10),
    `Displacement Power Factor B` VARCHAR(10),
    `Displacement Power Factor C` VARCHAR(10),
    `Displacement Power Factor Total` VARCHAR(10),
    `Frequency` FLOAT,
    `Power Factor Total IEC` FLOAT,
    `Power Factor Total Lead Lag` FLOAT,

    `Accumulated Energy Reset Date/Time` DATETIME,
    `Active Energy Delivered_Into Load` BIGINT,
    `Active Energy Received_Out of Load` BIGINT,
    `Active Energy Delivered+_Received` BIGINT,
    `Active Energy Delivered-_Received` BIGINT,

    `Apparent_Energy_Delivered` BIGINT,
    `Apparent_Energy_Received` BIGINT,
    `Apparent_Energy_Delivered+Received` BIGINT,
    `Apparent_Energy_Delivered-Received` BIGINT,
    `Power Demand_Method` SMALLINT UNSIGNED,
    `Power Demand_Interval Duration` SMALLINT UNSIGNED,
    `Power Demand_Subinterval Duration` SMALLINT UNSIGNED,
    `Power Demand_Elapsed Time in Interval` SMALLINT UNSIGNED,
    `Power Demand_Elapsed Time in Subinterval` SMALLINT UNSIGNED,
    `Power Demand_Peak Reset Date/Time` DATETIME,
    `Current Demand_Method` SMALLINT UNSIGNED,
    `Current Demand_Interval Duration` SMALLINT UNSIGNED,
    `Current Demand_Subinterval Duration` SMALLINT UNSIGNED,
    `Current Demand_Elapsed Time in Interval` SMALLINT UNSIGNED,
    `Current Demand_Elapsed Time in Subinterval` SMALLINT UNSIGNED,
    `Current Demand_Peak Reset Date/Time` DATETIME,
    `Demand System_Assignment` SMALLINT UNSIGNED,
    `Register_Number_of_Metered Quantity` SMALLINT UNSIGNED,
    `Units Code` SMALLINT UNSIGNED,
    `Last_Demand` FLOAT,
    `Present_Demand` FLOAT,
    `Predicted_Demand` FLOAT,
    `Peak_Demand` FLOAT,
    `Peak_Demand_DateTime` DATETIME
)
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()

print("Table 'POWER METER 1' created successfully.")

