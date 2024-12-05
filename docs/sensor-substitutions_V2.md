# FarmTech Solutions - Smart Irrigation System

This project is a **smart irrigation system** prototype designed for agricultural management using an ESP32 microcontroller. The system collects real-time data from various sensors, including temperature, humidity, and soil pH, and automates irrigation based on predefined thresholds. It also supports MQTT communication for data logging and remote control.

---

## 🚀 Features

- **Sensors**: Monitors temperature, humidity (DHT22), and soil pH (LDR-based).
- **Actuators**: Controls an irrigation pump through a relay module.
- **MQTT Integration**: Publishes sensor data and subscribes to commands.
- **LCD Display**: Displays real-time data for temperature, humidity, pH level, and irrigation status.
- **Wi-Fi Connectivity**: Uses ESP32 to connect to a Wi-Fi network.
- **Memory Monitoring**: Displays ESP32 heap memory statistics on the serial monitor.

---

## 🛠️ Hardware Components

1. **ESP32 Development Board**
2. **DHT22 Sensor** (for temperature and humidity)
3. **LDR Sensor** (for soil pH simulation)
4. **Relay Module** (to control the irrigation pump)
5. **Push Buttons** (to simulate nutrient levels: P and K)
6. **LCD Display (20x4)** with I2C interface
7. Resistors (10kΩ)
8. Power sources (e.g., USB)

---

## 🔌 Wiring Diagram

The wiring connections for the project are as follows:

- **DHT22 Sensor**:
    - `VCC` → `3V3`
    - `GND` → `GND`
    - `DATA` → GPIO `4`
- **LDR Sensor** (pH simulation):
    - `AO` → GPIO `34` (Analog input)
    - `VCC` → `3V3`
    - `GND` → `GND`
- **Relay Module**:
    - `IN` → GPIO `21`
    - `VCC` → `3V3`
    - `GND` → `GND`
- **Push Buttons**:
    - Button 1 (P): `1` → GPIO `19`, `2` → `GND`
    - Button 2 (K): `1` → GPIO `18`, `2` → `GND`
- **LCD Display**:
    - `VCC` → `3V3`
    - `GND` → `GND`
    - `SCL` → GPIO `22`
    - `SDA` → GPIO `21`

For more details, refer to the `diagram.json`.

---

## 💻 Software Requirements

- **Arduino IDE** (or PlatformIO)
- **Libraries**:
    - `DHT` (for temperature and humidity sensor)
    - `LiquidCrystal_I2C` (for LCD display)
    - `PubSubClient` (for MQTT)
    - `WiFi` (for ESP32 Wi-Fi)
- **Wi-Fi SSID**: `Wokwi-GUEST`
- **MQTT Broker**: `test.mosquitto.org`

---

## 📜 How It Works

1. **Initialization**:
    - Connects to the Wi-Fi network and MQTT broker.
    - Displays a welcome message on the LCD.

2. **Data Collection**:
    - Reads temperature and humidity from the DHT22 sensor.
    - Reads soil pH level using an LDR sensor.
    - Monitors button states to simulate nutrient levels.

3. **Irrigation Control**:
    - If humidity falls below 40%, the irrigation system is activated (relay is turned ON).

4. **Data Logging**:
    - Sends sensor data to the MQTT broker and serial monitor.
    - Data format:
      ```json
      {
        "temperature": 25.5,
        "humidity": 45.0,
        "ph": 6.5,
        "irrigation": 1
      }
      ```

5. **Remote Control**:
    - Subscribes to MQTT commands for external control.

---

## 🔧 Setup and Installation

1. Install the required libraries in Arduino IDE.
2. Connect the hardware as per the wiring diagram.
3. Upload the `main.cpp` code to the ESP32.
4. Open the serial monitor to observe real-time data and logs.

---

## 📈 Real-Time Monitoring

- **Serial Plotter**: Visualizes sensor data in real time.
- **LCD Display**: Provides local feedback on sensor readings and system status.
- **MQTT Dashboard**: Use an MQTT client (e.g., MQTT Explorer) to monitor or control the system.

---

## 📂 File Structure

- **diagram.json**: Circuit diagram for the project.
- **main.cpp**: Arduino sketch with the implementation logic.
- **README.md**: Project documentation (this file).

---

## 🤝 Contributions

Feel free to fork the repository and submit pull requests for improvements or new features!

---

## 📝 License

This project is open-source and licensed under the MIT License.