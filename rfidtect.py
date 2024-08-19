import serial.tools.list_ports
import csv
import time
import os
import asyncio

# Log file setup (continuing to use the CSV file)
log_file = "rfidetect.csv"

# Ensure log file exists and create it if not
if not os.path.exists(log_file):
    with open(log_file, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Tag ID", "Status"])  # Header row

# Function to log RFID detections and heartbeat messages
def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp}: {message}")  # Print the message for real-time feedback

    # Log the message to the CSV file
    with open(log_file, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, message, ""])

# Function to emit a beep sound 
def emit_beep():
    log_message("Beep emitted!")  # Log and print the beep event
    os.system('printf "\a"')  # Standard beep sound

# Function to display heartbeat message
async def heartbeat():
    while True:
        log_message("Heartbeat: Script is running...")
        await asyncio.sleep(5)  # Interval for the heartbeat message

# Function to scan a single port asynchronously
async def scan_port(port):
    log_message(f"Attempting to check port {port.device}...")

    try:
        ser = serial.Serial(port.device, baudrate=9600, timeout=0.5)
        log_message(f"Successfully opened port {port.device}")
        # The beep can be emitted here if this is a successful detection scenario.
        ser.close()
    except serial.SerialException as e:
        log_message(f"Error accessing {port.device}: {e}")

# Function to scan all available serial ports concurrently
async def scan_ports_concurrently():
    log_message("Scanning all available serial ports for RFID readers...")

    ports = serial.tools.list_ports.comports()

    if not ports:
        log_message("No serial ports found.")
        return
    
    tasks = [asyncio.ensure_future(scan_port(port)) for port in ports]
    tasks.append(asyncio.ensure_future(heartbeat()))

    await asyncio.gather(*tasks)

# Main entry point for the script
if __name__ == "__main__":
    asyncio.run(scan_ports_concurrently())
