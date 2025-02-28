import serial

BT_PORT = "COM3"
BT_BAUDRATE = 9600

try:
    bluetooth_serial = serial.Serial(BT_PORT, BT_BAUDRATE, timeout=1)
except serial.SerialException:
    bluetooth_serial = None
    print("Error: Bluetooth device not found.")

def get_moisture_level():
    if bluetooth_serial:
        moisture_data = bluetooth_serial.readline().decode().strip()
        return int(moisture_data) if moisture_data.isdigit() else 0
    return 0
