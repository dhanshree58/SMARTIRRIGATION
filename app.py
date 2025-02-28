from flask import Flask, render_template, request, jsonify
from control import toggle_motor
from input import set_crop_value
from moisture import get_moisture_level

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/control.html')
def control_page():
    return render_template('control.html')

@app.route('/input.html')
def input_page():
    return render_template('input.html')

@app.route('/realtime.html')
def realtime_page():
    return render_template('realtime.html')

# API for Motor Control (calls function in control.py)
@app.route('/toggle_motor', methods=['POST'])
def toggle_motor_api():
    return toggle_motor()

# API for Crop Input (calls function in input.py)
@app.route('/set_crop', methods=['POST'])
def set_crop_api():
    return set_crop_value()

# API to Get Moisture Data (calls function in moisture.py)
@app.route('/get_moisture', methods=['GET'])
def get_moisture_api():
    return jsonify({"moisture": get_moisture_level()})

if __name__ == '__main__':
    app.run(debug=True)
