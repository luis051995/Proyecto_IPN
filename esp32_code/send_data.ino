#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "TU_WIFI";
const char* password = "TU_PASS";
const char* serverName = "http://TU_IP:8000/api/sensor_data/";

int sensorPin = 34;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }
  Serial.println("Conectado al WiFi");
}

void loop() {
  int value = analogRead(sensorPin);
  Serial.println(value);

  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    String httpRequestData = "{\"acetona\":" + String(value) + ", \"usuario\":\"usuario1\", \"contrasena\":\"1234\"}";
    int httpResponseCode = http.POST(httpRequestData);

    Serial.println(httpResponseCode);
    http.end();
  }

  delay(5000);
}
