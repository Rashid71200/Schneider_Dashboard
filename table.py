import mysql.connector

# Establish a connection to your MySQL database
cnx = mysql.connector.connect(
    host='your_host',
    user='your_username',
    password='your_password',
    database='your_database'
)

# Create a cursor object
cursor = cnx.cursor()

# Define the SQL statement to create a table
create_table_query = """
CREATE TABLE your_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voltage FLOAT,
    current FLOAT,
    power FLOAT,
    energy FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

# Execute the SQL query to create the table
cursor.execute(create_table_query)

# Commit the changes to the database
cnx.commit()

# Close the cursor and database connection
cursor.close()
cnx.close()
