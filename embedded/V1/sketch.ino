#include <Arduino.h>
#include <DHT.h>

#define DHTPIN 4         // Pin for the DHT22 sensor
#define DHTTYPE DHT22    // Type of DHT sensor

#define P_SENSOR_PIN 19  // Pin for the button representing Nutrient P
#define K_SENSOR_PIN 18  // Pin for the button representing Nutrient K
#define PH_SENSOR_PIN 34 // Pin for the LDR representing pH
#define RELAY_PIN 21     // Pin for the relay (irrigation pump)

DHT dht(DHTPIN, DHTTYPE);

const int HUMIDITY_THRESHOLD = 40;

void setup() {
  Serial.begin(115200);
  pinMode(P_SENSOR_PIN, INPUT_PULLUP);
  pinMode(K_SENSOR_PIN, INPUT_PULLUP);
  pinMode(PH_SENSOR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  dht.begin();
  digitalWrite(RELAY_PIN, LOW);  // Initially, the relay is off
}

float mapAnalogToPH(int analogValue) {
    // Maps the analog value (0 to 4095 on ESP32) to a pH range (0 to 14)
    return analogValue * (14.0 / 4095.0);
}

void loop() {
  // Reading from the sensors
  int pSensor = digitalRead(P_SENSOR_PIN);
  int kSensor = digitalRead(K_SENSOR_PIN);
  int analogValue = analogRead(PH_SENSOR_PIN);
  float phLevel = mapAnalogToPH(analogValue);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Check for DHT22 sensor failure
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("DHT sensor read failure!");
    return;  // Exit the function on failure
  }

  // Display readings on the Serial Monitor
  Serial.print("Nutrient P: "); Serial.println(pSensor == LOW ? "OK" : "Low");
  Serial.print("Nutrient K: "); Serial.println(kSensor == LOW ? "OK" : "Low");
  Serial.print("pH: "); Serial.println(phLevel);
  Serial.print("Humidity: "); Serial.print(humidity); Serial.println("%");
  Serial.print("Temperature: "); Serial.print(temperature); Serial.println(" ÂºC");

  // Logic to turn the relay on/off (irrigation)
  if (humidity < HUMIDITY_THRESHOLD || pSensor == HIGH || kSensor == HIGH) {
    digitalWrite(RELAY_PIN, HIGH);  // Turn on the relay
    Serial.println("Irrigation: ON");
  } else {
    digitalWrite(RELAY_PIN, LOW);   // Turn off the relay
    Serial.println("Irrigation: OFF");
  }

  delay(2000);  // Delay for the next reading
}