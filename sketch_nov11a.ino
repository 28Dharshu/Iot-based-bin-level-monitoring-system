#define TRIG 9
#define ECHO 10
#define BUZZER 7

long duration;
int distance;
int threshold = 5; // distance in cm when dustbin is full

void setup() {
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Send ultrasonic signal
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  // Receive reflected signal
  duration = pulseIn(ECHO, HIGH);
  distance = duration * 0.034 / 2;  // Convert to centimeters

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Check if dustbin is full
  if (distance <= threshold) {
    Serial.println("Dustbin is FULL"); // 🔹 Important: signal for Python to send SMS
    digitalWrite(BUZZER, HIGH);
  } else {
    digitalWrite(BUZZER, LOW);
  }

  delay(1000);  // wait 1 second before next reading
}
