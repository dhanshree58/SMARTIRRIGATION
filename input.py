import serial
from flask import request, jsonify

BT_PORT = "COM3"
BT_BAUDRATE = 9600

try:
    bluetooth_serial = serial.Serial(BT_PORT, BT_BAUDRATE, timeout=1)
except serial.SerialException:
    bluetooth_serial = None
    print("Error: Bluetooth device not found.")

def set_crop_value():
    if bluetooth_serial:
        data = request.json
        crop_name = data.get("crop")

        if crop_name:
            bluetooth_serial.write(crop_name.encode())  # Send crop name to Arduino
            return jsonify({"message": f"Crop set to {crop_name}"})
        else:
            return jsonify({"error": "No crop name provided"}), 400
    else:
        return jsonify({"error": "Bluetooth not connected"}), 500
