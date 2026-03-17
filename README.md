# Smart Bin Level Monitoring System  
Using Arduino, Ultrasonic Sensor, Buzzer and SMS Alerts via Twilio API

---

## 1. Project Overview  
This IoT-based Smart Bin Monitoring System measures the fill level of a waste bin using an ultrasonic sensor.  

When the bin becomes full, the system triggers:

- Real-time readings on Serial Monitor  
- SMS alert to mobile using Twilio API  
- Buzzer alert  

The system is simple, reliable, and does not require Wi-Fi. It works using Arduino and a computer running a Python script for SMS alerts.

---

## 2. Features  
- Real-time ultrasonic distance measurement  
- Local buzzer alert  
- SMS notifications via Twilio  
- Serial Monitor output for monitoring  
- Lightweight Arduino code (no cloud or machine learning)  
- Fully offline operation  

---

## 3. Hardware Components  
- Arduino UNO / Mega  
- HC-SR04 Ultrasonic Sensor  
- Buzzer  
- Jumper wires  
- USB cable for serial communication  

---

## 4. Hardware Wiring Diagram  

![Hardware Wiring Diagram](https://raw.githubusercontent.com/28Dharshu/Iot-based-bin-level-monitoring-system/main/model%20image.png)

---

### Ultrasonic Sensor → Arduino  

| Ultrasonic Pin | Arduino Pin |
|----------------|-------------|
| VCC            | 5V          |
| GND            | GND         |
| TRIG           | D9          |
| ECHO           | D10         |

---

### Buzzer → Arduino  

| Buzzer Pin | Arduino Pin |
|------------|-------------|
| +          | D8          |
| -          | GND         |

---

## 5. Output Types  

### 5.1 Serial Monitor Output  
Displays:
- Real-time bin level distance  
- "BIN FULL" message when threshold is reached  

---

### 5.2 SMS Alert via Twilio  
When Arduino sends "FULL" through Serial, the Python script sends:

"Alert! Waste bin is FULL. Please clean."

---

### 5.3 Buzzer Alert  
The buzzer activates when the bin reaches the defined threshold.

---

## 6. Project File Structure  
- smart_bin.ino Arduino code for sensor and buzzer
- serial_to_twilio.py Python script for SMS alert
- model image.png Hardware wiring/model image
- README.md Project documentation

  
---

## 7. System Workflow  

Ultrasonic Sensor → Arduino → Serial Output → Python Script → Twilio API → User Mobile  

---

## 8. Software Requirements  
- Arduino IDE  
- Python 3  
- pySerial  
- Twilio Python SDK  
- Twilio Account (SID, Auth Token, Phone Number)  

---

## 9. How to Run  

### Step 1: Upload Arduino Code  
Open smart_bin.ino in Arduino IDE and upload it to the board.

### Step 2: Run Python Script  
python serial_to_twilio.py

The script listens to serial data and sends SMS when "FULL" is detected.

---

## 10. Twilio Configuration  
- Create a Twilio account  
- Get ACCOUNT SID, AUTH TOKEN, and Twilio phone number  
- Add them inside serial_to_twilio.py  

---

## 11. Applications  
- Smart waste management systems  
- Industrial containers  
- Hospitals and campuses  
- Public waste bins  
- Smart city solutions  
