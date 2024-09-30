# Real-Time Patient Monitoring App
## Overview
This project is a real-time patient monitoring system that uses sensors connected to an Arduino to collect vital signs such as heart rate and oxygen saturation (SpO2). The Arduino sends the data to a PC via Bluetooth, where the data is processed, visualized, and analyzed using a Python application. The app also includes features like anomaly detection (e.g., abnormal heart rate) and alerts.

## Features
* **Sensor Integration**: Collects data from various health sensors like a heart rate monitor (Pulse Sensor) and pulse oximeter (MAX30100/MAX30102).
* **Wireless Communication**: Uses Bluetooth to wirelessly transmit sensor data from the Arduino to a PC.
* **Real-Time Data Visualization**: Plots real-time graphs of vital signs such as heart rate and SpO2 using Python.
* **Anomaly Detection**: Detects abnormal readings (e.g., high or low heart rate) and triggers alerts.
* **Data Logging**: Stores historical data in a local SQLite database for further analysis.

## Hardware Requirements
* **Arduino**: Any Arduino board (e.g., Arduino Uno, Nano) with Bluetooth capabilities.
* **Option 1**: Arduino + Bluetooth module (HC-05 or HC-06).
* **Option 2**: Arduino Nano 33 BLE (has built-in Bluetooth).
* **Pulse Oximeter Sensor**: MAX30100, MAX30102, or MAX30105.
* **Heart Rate Sensor**: Pulse Sensor (or equivalent heart rate monitor).
* **Bluetooth-Enabled PC**: To receive the data from Arduino wirelessly.
* **Optional Sensors**: Temperature sensor (e.g., DHT11/DHT22).

## Software Requirements
* **Arduino IDE**: To upload code to the Arduino.
* **Python**: Version 3.x installed on your PC.
* **Python Libraries**:
  * pyserial: For Bluetooth communication.
  * matplotlib: For real-time data visualization.
  * sqlite3: For data storage.
  * tkinter: For the graphical user interface (GUI).
### Install Python Dependencies:
Install the required Python libraries by running:
```
pip install pyserial matplotlib sqlite3 tkinter
```

## Wiring Guide
### Pulse Oximeter (MAX30100/MAX30102)
* VCC → 3.3V (or 5V) on Arduino.
* GND → Ground on Arduino.
* SCL → SCL on Arduino (A5 on Uno/Nano).
* SDA → SDA on Arduino (A4 on Uno/Nano).
### Heart Rate Sensor (Pulse Sensor)
* VCC → 3.3V (or 5V) on Arduino.
* GND → Ground.
* Signal → A0 (Analog input).
### Bluetooth Module (HC-05/HC-06)
* VCC → 5V on Arduino.
* GND → Ground.
* TXD → RX (Pin 0) on Arduino (use a voltage divider for 3.3V logic).
* RXD → TX (Pin 1) on Arduino.

## Installation & Setup
1. Arduino Setup
   1. Connect the sensors and Bluetooth module to the Arduino as per the wiring guide.
   2. Upload the Arduino Code:
      * Open the provided Arduino sketch (arduino_code.ino) in the Arduino IDE.
      * Replace the sensor addresses/UUIDs if required (e.g., for MAX30100 sensor).
      * Upload the code to the Arduino.
    3. Pair the Bluetooth Module with Your PC:
     * Pair the Bluetooth module (HC-05/HC-06) with your PC via Bluetooth Settings.
     * Take note of the COM port assigned to the Bluetooth module (Windows) or the /dev/tty device (Linux/macOS).
  
```
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include "MAX30100_PulseOximeter.h"  // Library for MAX30100 sensor
#define REPORTING_PERIOD_MS 1000  // Report every 1 second

PulseOximeter pox;

void setup() {
    Serial.begin(9600);  // Initialize serial for debugging
    Serial1.begin(9600); // Initialize Bluetooth serial

    if (!pox.begin()) {
        Serial.println("Failed to initialize sensor");
        while (true);
    }

    pox.setOnBeatDetectedCallback(onBeatDetected);
}

void loop() {
    pox.update();
    if (millis() - lastReportTime > REPORTING_PERIOD_MS) {
        lastReportTime = millis();
        float heartRate = pox.getHeartRate();
        float SpO2 = pox.getSpO2();
        Serial1.print("Heart Rate: ");
        Serial1.print(heartRate);
        Serial1.print(" BPM, SpO2: ");
        Serial1.print(SpO2);
        Serial1.println(" %");
    }
}

void onBeatDetected() {
    Serial.println("Beat detected!");
}
```
       
2. Python Application Setup
    1. Clone or Download this repository on your PC.
    2. Edit the Bluetooth Port:

      * In the Python application (app.py), update the BLUETOOTH_PORT variable with the correct port for your Bluetooth module.
         - Example for Windows: COM3.
         - Example for Linux/macOS: /dev/tty.HC-05-DevB.
    3. Run the Application:

        Run the Python application to start reading data from the Arduino:
```
python app.py
```

## Project Structure

- patient_monitoring_app/
- │
- ├── app.py              # Main application entry point
- ├── sensor.py           # Sensor communication via Bluetooth
- ├── data_processing.py  # Data processing and anomaly detection
- ├── visualization.py    # Real-time data visualization with matplotlib
- ├── database.py         # Database interaction (SQLite)
- └── gui.py              # Graphical User Interface (Tkinter)

### File Descriptions:
* **app.py**: Coordinates all the modules (sensor reading, data processing, visualization, and GUI).
* **sensor.py**: Handles Bluetooth communication to receive sensor data from Arduino.
* **data_processing.py**: Contains functions to process heart rate and SpO2 data, and detect anomalies.
* **visualization.py**: Visualizes heart rate and SpO2 data in real time using matplotlib.
* **database.py**: Logs sensor data into an SQLite database for historical analysis.
* **gui.py**: Manages the user interface (Tkinter) to display real-time data and alerts.

## How It Works
1. Arduino:
   * The Arduino collects heart rate and SpO2 data from the sensors and sends it over Bluetooth.
2. Python Application:
   * Bluetooth Communication: Python receives data from the Arduino via Bluetooth using pyserial.
   * Data Processing: The received data is processed and checked for anomalies (e.g., heart rate too high or low).
   * Visualization: The app plots real-time graphs of heart rate and SpO2 data using matplotlib.
   * Alerts: Alerts are displayed if any anomalies are detected in the sensor readings.
   * Data Logging: All the sensor data is logged into an SQLite database for later analysis.

## Usage
1. Launch the Arduino with the sensors connected and Bluetooth module powered on.
2. Pair the Arduino's Bluetooth module (HC-05 or HC-06) with your PC.
3. Run the Python Application to start monitoring the vital signs in real-time.
   * The data will be displayed in the GUI, and alerts will trigger if abnormal values are detected.
4. View Historical Data: Historical sensor data is saved in an SQLite database for future analysis.

##Troubleshooting
* No Data on Python Application: Ensure that the correct Bluetooth COM port is set in the app.py file. Verify that the Arduino is paired and sending data correctly.
* Invalid Sensor Readings: Double-check wiring and sensor connections on the Arduino. Ensure the correct libraries are installed on the Arduino for the sensor.
* Bluetooth Issues: Try resetting the Bluetooth module or re-pairing the device if the connection is unstable.

## Future Improvements
* Add more sensors: Extend the project by adding temperature, ECG, or other vital sign sensors.
* Cloud Integration: Upload data to the cloud for remote monitoring.
* Mobile App: Develop a mobile app to receive and display the sensor data wirelessly.

## License
This project is licensed under the MIT License.

## Contributors
[Carolina Guinart](https://github.com/Karolkalex)
