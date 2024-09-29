import asyncio
import threading
import tkinter as tk

from sensor import Sensor
from data_processing import process_heart_rate, detect_anomaly
from database import init_db, insert_heart_rate
from visualization import Visualizer
from gui import GUI

SENSOR_ADDRESS = "DEVICE_BLUETOOTH_ADDRESS"

# Initialize the sensor
sensor = Sensor(SENSOR_ADDRESS)

async def fetch_data():
    await sensor.connect()
    while True:
        heart_rate = await sensor.get_heart_rate()
        heart_rate = process_heart_rate(heart_rate)
        insert_heart_rate(heart_rate)
        if detect_anomaly(heart_rate):
            print(f"Anomaly detected: {heart_rate}")
        return heart_rate

def start_event_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def heart_rate_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(fetch_data())

def main():
    # Initialize database
    init_db()

    # Setup the real-time visualizer
    visualizer = Visualizer()

    # Run the tkinter GUI in the main thread
    root = tk.Tk()
    gui = GUI(root, heart_rate_callback)
    root.title("Patient Monitoring App")
    
    # Create a separate thread for fetching data and updating graphs
    event_loop = asyncio.new_event_loop()
    loop_thread = threading.Thread(target=start_event_loop, args=(event_loop,), daemon=True)
    loop_thread.start()

    root.mainloop()

    # Start real-time visualization
    visualizer.start_visualization()

if __name__ == "__main__":
    main()