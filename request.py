import requests
import asyncio

url = 'http://127.0.0.1:5000/data1'  # Replace this with the actual server address

# Sample data to be sent
data_to_send = {
    'key1': 6969,
    'key2': 543,
    'key3': 123,
    'key3': 675
}

async def send_data():
    while True:
        try:
            # Sending data to the server using POST request
            response = requests.post(url, json=data_to_send)

            if response.status_code == 200:
                data_received = response.json()
                print("Data sent successfully.")
                print("Received data from the server:")
                print(data_received)
            else:
                print(f"Failed to send data. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
        
        await asyncio.sleep(5)  # Wait for 5 seconds before sending data again

async def main():
    # Start the send_data() function as a task
    send_data_task = asyncio.create_task(send_data())
    
    # Your other code or tasks can be added here if needed

    # Wait for the send_data_task to finish (which will never happen in this case)
    await send_data_task

if __name__ == "__main__":
    asyncio.run(main())
