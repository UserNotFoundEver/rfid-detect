# RFID Detection Script

This repository contains a Python script designed to detect RFID devices connected to your system via serial ports. It provides real-time feedback and logs relevant information to a CSV file. RFID scanning or interference may be illegal in certain locations. This is for security purposes only. Further and custom development is needed for better results and Operations. All Federal Laws apply to use this script.

## Features

- **Heartbeat Monitoring**: Displays a "Script is running..." message every 5 seconds to ensure the script is active.
- **Serial Port Scanning**: Automatically scans all available serial ports, filtering out irrelevant ports like Bluetooth.
- **Beep Alerts**: Emits a beep sound upon detecting an RFID device or when specific events occur.
- **Logging**: Logs all activity, including port scans and detections, to a CSV file (`rfidetect.csv`) for easy tracking.

## Requirements

- Python 3.x
- `pyserial` library for serial communication
- Compatible with macOS (other platforms may require modifications)

## Install Required Libraries:

## Run the script! 
sudo python3 rfidtect.py

## License
We use The Unlicense. You may donate to this eth address if you find this or other tools helpful. 

0xa9aeE5ed1b5fF1cC503298328dEfe11f6C0D2A8e