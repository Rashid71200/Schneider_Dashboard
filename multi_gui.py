from pymodbus.client.sync import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder, Endian
import tkinter as tk
import webbrowser

# Modbus Slave 1 configuration
slave1_client = ModbusSerialClient(
    method='rtu',
    port='COM11',
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1
)


# Function to update text values for Modbus Slave 1
def update_text_slave1(canvas):
    try:
        slave1_client.connect()

        response1 = slave1_client.read_holding_registers(address=3019, count=2, unit=1)
        response2 = slave1_client.read_holding_registers(address=3009, count=2, unit=1)
        response3 = slave1_client.read_holding_registers(address=3059, count=2, unit=1)
        response4 = slave1_client.read_holding_registers(address=3109, count=2, unit=1)

        if response1.isError():
            print(f"Request error: {response1}")
        else:
            decoder = BinaryPayloadDecoder.fromRegisters(response1.registers, Endian.Big, wordorder=Endian.Big)
            canvas.itemconfig(text1, text=str(round(decoder.decode_32bit_float(), 2)))

            decoder1 = BinaryPayloadDecoder.fromRegisters(response2.registers, Endian.Big, wordorder=Endian.Big)
            canvas.itemconfig(text2, text=str(round(decoder1.decode_32bit_float(), 2)))

            decoder2 = BinaryPayloadDecoder.fromRegisters(response3.registers, Endian.Big, wordorder=Endian.Big)
            canvas.itemconfig(text3, text=str(round(decoder2.decode_32bit_float(), 2)))

            decoder3 = BinaryPayloadDecoder.fromRegisters(response4.registers, Endian.Big, wordorder=Endian.Big)
            canvas.itemconfig(text5, text=str(round(decoder3.decode_32bit_float(), 2)))

            root.after(1000, update_text_slave1, canvas)

    except Exception as e:
        print("Error:", e)

    finally:
        slave1_client.close()

# Function to update text values for Modbus Slave 2
def update_text_slave2(canvas):
    try:

        slave1_client.connect()

        # Read holding register values for Slave 2
        # Customize the register addresses, counts, and units as per your requirements
        response1 = slave1_client.read_holding_registers(address=3019, count=2, unit=2)
        response2 = slave1_client.read_holding_registers(address=3009, count=2, unit=2)
        response3 = slave1_client.read_holding_registers(address=3059, count=2, unit=2)
        response4 = slave1_client.read_holding_registers(address=3109, count=2, unit=2)

        # Update the text values on the canvas for Slave 2

        root1.after(1000, update_text_slave2, canvas)

    except Exception as e:
        print("Error:", e)

    finally:
        slave1_client.close()

# Function to open link in a web browser
def open_link(event):
    webbrowser.open("https://ahrneloy.github.io/")

# Create the main window for Slave 1
root = tk.Tk()
root.geometry("832x861")
canvas = tk.Canvas(root, width=832, height=861)
canvas.pack()
image = tk.PhotoImage(file="Schneider_meter1.png")
canvas.create_image(0, 0, anchor="nw", image=image)
text1 = canvas.create_text(400, 284, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text2 = canvas.create_text(400, 361, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text3 = canvas.create_text(400, 435, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text5 = canvas.create_text(400, 512, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text4 = canvas.create_text(400, 832, text="©Azaharul Rashid", fill="#e0e0e4", font=("Arial", 22, "bold"), anchor="center")
canvas.tag_bind(text4, "<Button-1>", open_link)
canvas.tag_bind(text4, "<Enter>", lambda e: canvas.itemconfig(text4, fill="red"))
canvas.tag_bind(text4, "<Leave>", lambda e: canvas.itemconfig(text4, fill="blue"))

# Create the main window for Slave 2
root1 = tk.Tk()
root1.geometry("832x861")
canvas1 = tk.Canvas(root1, width=832, height=861)
canvas1.pack()
image1 = tk.PhotoImage(file="C:\\Users\\AhrNiloy\\Desktop\\mobus-main\\tomorrow\\f\\Schneider_meter1.png", master=root1)
#image1 = tk.PhotoImage(file="C:\Users\AhrNiloy\Desktop\mobus-main\tomorrow\Schneider_meter1.png"
canvas1.create_image(0, 0, anchor="nw", image=image1)
# Create and place the text labels for Slave 2
# Customize the text positions and other properties as per your requirements
text6 = canvas1.create_text(400, 200, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text7 = canvas1.create_text(400, 300, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text8 = canvas1.create_text(400, 400, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text9 = canvas1.create_text(400, 500, text="", fill="black", font=("Arial", 35, "bold"), anchor="center")
text10 = canvas1.create_text(400, 800, text="©Azaharul Rashid", fill="#e0e0e4", font=("Arial", 22, "bold"), anchor="center")
canvas1.tag_bind(text10, "<Button-1>", open_link)
canvas1.tag_bind(text10, "<Enter>", lambda e: canvas1.itemconfig(text10, fill="red"))
canvas1.tag_bind(text10, "<Leave>", lambda e: canvas1.itemconfig(text10, fill="blue"))

# Start updating text values for Slave 1
update_text_slave1(canvas)

# Start updating text values for Slave 2
update_text_slave2(canvas1)

# Start the main loop for Slave 1
root.mainloop()

# Start the main loop for Slave 2
root1.mainloop()
