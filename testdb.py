import mysql.connector

# Replace these values with your actual MySQL server configuration
host = 'localhost'
user = 'root'
password = '$n200000G'
database = 'power_meter'
table_name = 'POWER_METER_1'

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Create a cursor to interact with the database
cursor = connection.cursor()

# SQL query to get the column count for the specified table
get_column_count_query = f"SELECT COUNT(*) FROM information_schema.columns WHERE table_schema = '{database}' AND table_name = '{table_name}'"

# Execute the query
cursor.execute(get_column_count_query)

# Fetch the result
column_count = cursor.fetchone()[0]

# Close the cursor and the connection
cursor.close()
connection.close()

# Print the column count
print(f"The table '{table_name}' has {column_count} columns.")
