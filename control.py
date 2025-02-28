import serial
import time
from flask import request, jsonify

BT_PORT = "COM3"  # Update based on your system
BT_BAUDRATE = 9600

try:
    bluetooth_serial = serial.Serial(BT_PORT, BT_BAUDRATE, timeout=1)
    time.sleep(2)
except serial.SerialException:
    bluetooth_serial = None
    print("Error: Bluetooth device not found.")

def toggle_motor():
    if bluetooth_serial:
        data = request.json
        motor_status = data.get("motor_status")

        if motor_status == "ON":
            bluetooth_serial.write(b'1')
        else:
            bluetooth_serial.write(b'0')

        return jsonify({"message": f"Motor turned {motor_status}"})
    else:
        return jsonify({"error": "Bluetooth not connected"}), 500
