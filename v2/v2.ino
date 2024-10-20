#include <DHT.h>

#define DHTPIN A2          // Pin where the DHT sensor is connected
#define DHTTYPE DHT11     // DHT 11 or DHT22
DHT dht(DHTPIN, DHTTYPE);

#define MOISTURE_PIN A0   // Soil moisture sensor pin

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // Read humidity and temperature
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Read soil moisture
  int soilMoisture = analogRead(MOISTURE_PIN)*100/1023;

  // Send data to Python
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(soilMoisture);

  // Wait before sending the next reading
  delay(2000);
}