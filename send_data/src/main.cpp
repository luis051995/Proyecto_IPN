#include <WiFi.h>
#include <BluetoothSerial.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>

const char* ssid = "INFINITUM12AF";
const char* password = "kEY7AWZN22";

BluetoothSerial SerialBT;
AsyncWebServer server(80);

const int sensorPin = 34;
float R0 = 10.0;

float calculatePPM(int analogValue) {
  float voltage = analogValue * (3.3 / 4095.0);
  float RS = (3.3 - voltage) / voltage;
  float ratio = RS / R0;
  float ppm = pow(10, ((log10(ratio) - 0.4) / -0.38));
  return ppm;
}

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32_MQ138");

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando a WiFi...");
  }
  Serial.println("Conectado a WiFi");

  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    int analogValue = analogRead(sensorPin);
    float ppm = calculatePPM(analogValue);
    String message = "Concentración de gas: " + String(ppm, 2) + " ppm";
    request->send(200, "text/plain", message);
  });

  server.begin();
}

void loop() {
  int analogValue = analogRead(sensorPin);
  float ppm = calculatePPM(analogValue);

  if (SerialBT.hasClient()) {
    SerialBT.printf("Concentración de gas: %.2f ppm\n", ppm);
  }

  Serial.printf("PPM: %.2f\n", ppm);
  delay(1000);
}
