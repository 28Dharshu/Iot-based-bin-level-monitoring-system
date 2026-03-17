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

<p align="center">
  <img src="https://raw.githubusercontent.com/28Dharshu/Iot-based-bin-level-monitoring-system/main/model%20image.jpg" width="500">
</p>

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

## 6. Output Results  

### 6.1 Serial Monitor Output  

<p align="center">
  <img src="https://raw.githubusercontent.com/28Dharshu/Iot-based-bin-level-monitoring-system/main/serial_output.png" width="400">
</p>

---

### 6.2 SMS Output  

<p align="center">
  <img src="https://raw.githubusercontent.com/28Dharshu/Iot-based-bin-level-monitoring-system/main/sms_output.png" width="400">
</p>

---

### 6.3 Buzzer Output  

The buzzer produces a sound alert when the bin is full, providing immediate local notification.

---

## 7. Project Workflow  

### Step-by-Step Working Process  

1. The ultrasonic sensor continuously measures the distance between the sensor and the waste level.  
2. The Arduino processes the distance data and compares it with a predefined threshold value.  
3. If the measured distance is greater than the threshold, the system continues monitoring.  
4. If the measured distance is less than or equal to the threshold:  
   - The bin is considered full  
   - Arduino sends "FULL" through Serial  
   - Buzzer is activated  
5. The Python script reads the Serial data continuously.  
6. When "FULL" is detected:  
   - Twilio API is triggered  
   - SMS is sent to the user  
7. The user receives the alert and takes action.

---

### Workflow Diagram  

<p align="center">
  <img src="https://raw.githubusercontent.com/28Dharshu/Iot-based-bin-level-monitoring-system/main/working_diagram.png" width="500">
</p>

---

## 8. Project File Structure  

smart_bin.ino
serial_to_twilio.py
model image.png
workflow_diagram.png
serial_output.png
sms_output.png
README.md


---

## 9. Software Requirements  
- Arduino IDE  
- Python 3  
- pySerial  
- Twilio Python SDK  
- Twilio Account (SID, Auth Token, Phone Number)  

---

## 10. How to Run  

### Step 1: Upload Arduino Code  
Open `smart_bin.ino` in Arduino IDE and upload it to the board.

### Step 2: Run Python Script  


The script listens to serial data and sends SMS when "FULL" is detected.

---

## 11. Twilio Configuration  
- Create a Twilio account  
- Get ACCOUNT SID, AUTH TOKEN, and Twilio phone number  
- Add them inside `serial_to_twilio.py`  

---

## 12. Applications  
- Smart waste management systems  
- Industrial containers  
- Hospitals and campuses  
- Public waste bins  
- Smart city solutions  
python serial_to_twilio.py
