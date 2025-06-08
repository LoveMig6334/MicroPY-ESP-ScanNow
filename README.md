# 📱 ESP-Scanner: IoT Card Scanner with ESP32 and MicroPython

A simple yet powerful RFID/NFC card scanner project built using ESP32 microcontrollers and MicroPython.

## 🔍 Overview

ESP-Scanner is an IoT-based card scanning solution that leverages the power of ESP32 microcontrollers and MicroPython to read, process, and transmit card data. This project can be used for access control systems, attendance tracking, payment systems, or any application requiring card identification.

## ✨ Features

- RFID/NFC card reading capabilities
- WiFi connectivity for data transmission
- Simple and clean MicroPython implementation
- Low power consumption
- Customizable behavior through configuration files
- LED status indicators
- Optional web interface for management

## 🛠️ Hardware Requirements

- ESP32 development board (ESP32-WROOM, ESP32-DevKitC, etc.)
- MFRC522 RFID reader module or PN532 NFC module
- Jumper wires
- Micro USB cable
- Optional: LEDs, buzzer, case

## 💻 Software Requirements

- Python 3.6 or newer
- esptool (for flashing MicroPython)
- ampy or rshell (for file transfer)
- MicroPython firmware for ESP32
- Terminal program (like PuTTY, Minicom, or Screen)

## 📥 Installation

### 1. Install Required Tools

```bash
pip install esptool
pip install adafruit-ampy
```

### 2. Download MicroPython Firmware

Download the latest stable MicroPython firmware for ESP32 from [MicroPython Downloads](https://micropython.org/download/esp32/).

### 3. Connect ESP32 to Computer

Connect your ESP32 board to your computer using a Micro USB cable.

### 4. Erase ESP32 Flash

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```
(Replace `/dev/ttyUSB0` with your actual port, on Windows it might be `COM3` or similar)

### 5. Flash MicroPython Firmware

```bash
esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 esp32-20220117-v1.18.bin
```
(Replace the firmware filename with your downloaded version)

### 6. Upload Project Files

```bash
ampy --port /dev/ttyUSB0 put main.py
ampy --port /dev/ttyUSB0 put config.py
# Upload any additional files
```

### 7. Wiring the RFID/NFC Module

Connect the MFRC522 module to ESP32:
- 3.3V → 3.3V
- GND → GND
- MISO → GPIO19
- MOSI → GPIO23
- SCK → GPIO18
- SDA/SS → GPIO5
- RST → GPIO22

## ⚙️ Configuration

Edit the `config.py` file to set your WiFi credentials and other settings:

```python
WIFI_SSID = "Your_WiFi_Name"
WIFI_PASSWORD = "Your_WiFi_Password"
SERVER_URL = "http://your-server.com/api/scan"
```

## 📝 Usage

1. Power the ESP32 using a USB cable or external power supply
2. The device will automatically connect to the configured WiFi network
3. Present a card to the RFID/NFC reader
4. The ESP32 will read the card data and process it according to the program
5. LED indicators will show the status of the operation

## 🔧 Troubleshooting

- **Device not connecting to WiFi**: Check your credentials in the config file
- **RFID reader not detecting cards**: Verify the wiring connections
- **Upload errors**: Ensure you're using the correct port and have proper permissions

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- MicroPython community
- ESP32 developers
- Contributors to MFRC522/PN532 libraries
