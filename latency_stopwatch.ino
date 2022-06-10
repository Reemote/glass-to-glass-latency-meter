const boolean LED_ON = HIGH;
const boolean LED_OFF = LOW;

const byte RED_LED = 11;
const byte GREEN_LED = 12;
const byte BLUE_LED = 13;

const int PHOTO_SENSOR_THRESHOLD_VALUE = 900;
const int PHOTO_SENSOR_PIN = A0;

boolean ledTimestampSet = false;
unsigned long ledOnTimestamp = 0;

unsigned long latency;

void setup() {
  Serial.begin(9600);
  
  pinMode(RED_LED, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
}

void loop() {
  if (!ledTimestampSet) {
    digitalWrite(GREEN_LED, LED_ON);
    
    ledOnTimestamp = millis();
    ledTimestampSet = true; 
  }
  
  int photoSensorValue = analogRead(PHOTO_SENSOR_PIN);  
  
  if (photoSensorValue > PHOTO_SENSOR_THRESHOLD_VALUE) {
    unsigned long photoSensorCaptureTimestamp = millis();
    latency = photoSensorCaptureTimestamp - ledOnTimestamp;
    
    Serial.println(latency);

    ledTimestampSet = false;
    digitalWrite(GREEN_LED, LED_OFF);
    delay(1000);
  }
}
