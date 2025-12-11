# serial_to_twilio.py
# Listens to Arduino serial. When it sees "FULL" in any line, it sends an SMS via Twilio.

import time
import os
import sys
from twilio.rest import Client
import serial
import serial.tools.list_ports

# ========== CONFIG ==========
TWILIO_SID    = os.getenv("TWILIO_SID", "Insert Twilio API Key")
TWILIO_TOKEN  = os.getenv("TWILIO_TOKEN", "Insert the Twilio token")
TWILIO_FROM   = os.getenv("TWILIO_FROM", "Insert Twilio phone number")     # Your Twilio phone number
TO_NUMBER     = os.getenv("TO_NUMBER", "Insert Recipient Phone number")      # Recipient phone number
SERIAL_PORT   = os.getenv("SERIAL_PORT", "COM8")             # Example: COM8 on Windows
BAUDRATE      = int(os.getenv("BAUDRATE", "9600"))
COOLDOWN_SEC  = int(os.getenv("COOLDOWN_SEC", "1800"))       # 30 min cooldown
HEARTBEAT_SEC = 10  # Print waiting heartbeat every 10 seconds
# ============================

client = Client(TWILIO_SID, TWILIO_TOKEN)

def send_sms(body):
    """Send an SMS message using Twilio."""
    try:
        message = client.messages.create(body=body, from_=TWILIO_FROM, to=TO_NUMBER)
        print(f"[{time.strftime('%H:%M:%S')}] ✅ SMS sent successfully! SID: {message.sid}")
        return True
    except Exception as e:
        print(f"[{time.strftime('%H:%M:%S')}] ❌ Twilio error: {e}")
        return False

def list_ports_print():
    ports = list(serial.tools.list_ports.comports())
    if not ports:
        print("No serial ports found.")
        return
    print("Available serial ports:")
    for p in ports:
        print(f"  {p.device}  -  {p.description}  [{p.hwid}]")

def open_serial(port, baud):
    """Try to open the serial port safely."""
    try:
        ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)  # give Arduino time to reset
        print(f"Opened serial {port} at {baud}bps")
        return ser
    except PermissionError as e:
        print(f"⚠️ PermissionError opening {port}: {e}")
        print("Close Arduino Serial Monitor or any app using this port.")
        list_ports_print()
        return None
    except serial.SerialException as e:
        print(f"⚠️ SerialException opening {port}: {e}")
        list_ports_print()
        return None
    except Exception as e:
        print(f"⚠️ Could not open serial port: {e}")
        list_ports_print()
        return None

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("--list-ports", "-l"):
        list_ports_print()
        return

    print("🔌 Starting serial → Twilio bridge")
    print(f"Configured SERIAL_PORT={SERIAL_PORT}, BAUDRATE={BAUDRATE}")
    ser = open_serial(SERIAL_PORT, BAUDRATE)
    if ser is None:
        print("❌ Exiting due to serial open failure.")
        return

    last_alert_time = 0
    last_heartbeat = time.time()

    try:
        while True:
            try:
                raw = ser.readline()
            except Exception as e:
                print("Serial read error:", e)
                break

            now = time.time()
            if now - last_heartbeat >= HEARTBEAT_SEC:
                print(f"[{time.strftime('%H:%M:%S')}] Waiting for serial data...")
                last_heartbeat = now

            if not raw:
                continue

            try:
                line = raw.decode('utf-8', errors='ignore').strip()
            except Exception:
                line = raw.decode('latin1', errors='ignore').strip()

            if not line:
                continue

            print(f"[{time.strftime('%H:%M:%S')}] RX: {line}")

            # ✅ Detect any line containing 'FULL'
            if "FULL" in line.upper():
                if now - last_alert_time >= COOLDOWN_SEC:
                    print("🚨 FULL detected — sending SMS...")
                    body = "🚮 Alert: Dustbin is full. Please collect."
                    if send_sms(body):
                        last_alert_time = now
                else:
                    remaining = int(COOLDOWN_SEC - (now - last_alert_time))
                    print(f"⏳ Cooldown active. {remaining}s remaining before next SMS.")

            # Optional test command
            elif line.upper() == "TEST":
                print("🧪 TEST command received — sending test SMS...")
                send_sms("Test alert from Smart Waste Bin system (Python).")

    except KeyboardInterrupt:
        print("\n🛑 Exiting on user interrupt (CTRL+C).")
    finally:
        if ser:
            ser.close()
            print("Serial closed.")

if __name__ == "__main__":
    main()
