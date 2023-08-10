basket = {
    'POWER_METER_4': '127.0.0.2'
}

if __name__ == "__main__":
    # Iterate through the keys (table names) in the basket dictionary
    for table_name in basket.keys():
        print(f"Processing table: {table_name}")

        # Perform actions for each table here, such as creating a table or inserting data

        # For example, you can create a connection and create a table
        # connection = mysql.connector.connect(host="your_host", user="your_user", password="your_password", database="your_database")
        # create_table(connection, table_name, fruts_list)

        # Close the connection when done
        # connection.close()

    print("All tables processed.")