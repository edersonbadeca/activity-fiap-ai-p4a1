#include <Arduino.h>
#include <DHT.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <WiFi.h>
#include <PubSubClient.h>


#define ssid "Wokwi-GUEST"
#define password ""

const char* mqtt_broker = "test.mosquitto.org";
const int mqtt_port = 1883;

const char* mqtt_topic_publish = "esp32/sensors";
const char* mqtt_topic_subscribe = "esp32/commands";

#define DHTPIN 4         // Pin for the DHT22 sensor
#define DHTTYPE DHT22    // Type of DHT sensor

#define P_SENSOR_PIN 19  // Pin for the button representing Nutrient P
#define K_SENSOR_PIN 18  // Pin for the button representing Nutrient K
#define PH_SENSOR_PIN 34 // Pin for the LDR representing pH
#define RELAY_PIN 21     // Pin for the relay (irrigation pump)

DHT dht(DHTPIN, DHTTYPE);
LiquidCrystal_I2C lcd(0x27, 16, 2);  // LCD I2C address, 16x2 display

WiFiClient espClient;
PubSubClient client(espClient);

const int HUMIDITY_THRESHOLD = 40;

/**
 * Initializes the WiFi connection.
 * Connects to the specified WiFi network and waits until the connection is established.
 * Prints the connection status to the Serial monitor.
 */
void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  lcd.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    lcd.print('.');
    delay(1000);
  }
  lcd.clear();
  lcd.print("\nConnected to WiFi");
  delay(2000);
  lcd.clear();
  lcd.print("IP Address: " + WiFi.localIP().toString());
  delay(2000);
  lcd.clear();
}

/**
 * Callback function that handles incoming MQTT messages.
 * This function is called when a message is received on a subscribed topic.
 *
 * @param topic The topic on which the message was received.
 * @param payload The message payload.
 * @param length The length of the message payload.
 */
void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);

  Serial.print("Message: ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)message[i]);
  }
  Serial.println();
}

/**
 * Initializes the MQTT client.
 * Sets the server and the callback function for the MQTT client.
 * Attempts to connect to the MQTT broker and subscribes to the necessary topics.
 */
void initMQTT() {
  client.setServer(mqtt_broker, mqtt_port);
  client.setCallback(callback);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT broker");
      client.subscribe(mqtt_topic_subscribe);
    } else {
      Serial.print("Failed with state ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

/**
 * Sets up the initial configuration for the microcontroller.
 * Initializes the serial communication, LCD display, DHT sensor, WiFi, and MQTT client.
 * Configures the pins and sets the initial state for the relay.
 */
void setup() {
  Serial.begin(115200);

  // Initialize pins
  pinMode(P_SENSOR_PIN, INPUT_PULLUP);
  pinMode(K_SENSOR_PIN, INPUT_PULLUP);
  pinMode(PH_SENSOR_PIN, INPUT);
  pinMode(RELAY_PIN, OUTPUT);

  // Initialize DHT sensor and LCD
  dht.begin();
  lcd.init();  // initialize the lcd
  lcd.backlight();  // Turn on the LCD backlight

  // Welcome message on LCD
  lcd.setCursor(0, 0);
  initWiFi();
  lcd.print("FarmTech Solutions");
  lcd.setCursor(0, 1);
  lcd.print("Initializing...");
  initMQTT();
  delay(2000);
  lcd.clear();
}

/**
 * Maps the analog value from the pH sensor to a pH level.
 *
 * @param analogValue The analog value read from the pH sensor.
 * @return The corresponding pH level.
 */
float mapAnalogToPH(int analogValue) {
  return analogValue * (14.0 / 4095.0);
}



void memoryCheck() {
  Serial.print("Free Heap: ");
  Serial.print(ESP.getFreeHeap() / 1.0e6, 2);  // Convertendo para MB com 2 casas decimais
  Serial.println(" MB");

  Serial.print("Max Allocatable Heap: ");
  Serial.print(ESP.getMaxAllocHeap() / 1.0e6, 2);  // Convertendo para MB com 2 casas decimais
  Serial.println(" MB");

  Serial.print("Total Heap Size: ");
  Serial.print(ESP.getHeapSize() / 1.0e6, 2);  // Convertendo para MB com 2 casas decimais
  Serial.println(" MB");

  delay(2000);  // Atualiza a cada 2 segundos
}

/**
 * Main loop function that runs continuously.
 * Reads sensor values, updates the LCD display, and controls the irrigation system.
 * Also handles MQTT client loop and publishes sensor data.
 */
void loop() {
  memoryCheck();
  client.loop(); 
  
  int pSensor = digitalRead(P_SENSOR_PIN);
  int kSensor = digitalRead(K_SENSOR_PIN);
  int analogValue = analogRead(PH_SENSOR_PIN);
  float phLevel = mapAnalogToPH(analogValue);
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    lcd.setCursor(0, 0);
    lcd.print("DHT Error!");
    return;
  }

  
  lcd.setCursor(0, 0);
  lcd.print("Temp: ");
  lcd.print(temperature, 1);
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("Hum: ");
  lcd.print(humidity, 1);
  lcd.print("%");

  lcd.setCursor(0, 2);
  lcd.print("pH: ");
  lcd.print(phLevel, 1);

  lcd.setCursor(0, 3);
  bool irrigation = humidity < HUMIDITY_THRESHOLD;
  if (irrigation) {
    digitalWrite(RELAY_PIN, HIGH);
    lcd.print("Irrigation: ON ");
  } else {
    digitalWrite(RELAY_PIN, LOW);
    lcd.print("Irrigation: OFF");
  }
  Serial.println("Send data to Serial Plotter");
  Serial.print(temperature);
  Serial.print("\t");  
  Serial.print(humidity); 
  Serial.print("\t");
  Serial.print(phLevel);
  Serial.print("\t");
  Serial.println(humidity < HUMIDITY_THRESHOLD ? 1 : 0);
  delay(5000); 

  String payload = "{";
  payload += "\"temperature\":" + String(temperature, 1) + ",";
  payload += "\"humidity\":" + String(humidity, 1) + ",";
  payload += "\"ph\":" + String(phLevel, 1) + ",";
  payload += "\"irrigation\":" + String(irrigation ? "1" : "0");
  payload += "}";

  client.publish(mqtt_topic_publish, payload.c_str());
  Serial.println("Published: " + payload);

  delay(2000); 
}
