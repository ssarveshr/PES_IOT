#include "DHT.h"
#define DHTPIN A2    // Pin connected to the data pin of DHT11
#define DHTTYPE DHT11  // DHT11 sensor
DHT dht(DHTPIN, DHTTYPE);
const int sensorPin1 = A0;
const int sensorPin2 = A1;
// Variables to store sensor values
int sensorValue1 = 0;
int sensorValue2 = 0;
int percentMoisture1 = 0;
int percentMoisture2 = 0;
// Dry and wet values for calibration (depends on your sensor and setup)
int dryValue = 1010;   
int wetValue = 300;    
void setup() {
  // Start the serial communication to output data to the serial monitor
  Serial.begin(9600);
  pinMode(sensorPin1, INPUT);
  pinMode(sensorPin2, INPUT);  
  dht.begin();  
}
void loop() {
  // Read the analog value from the sensor
  sensorValue1 = analogRead(sensorPin1);
  sensorValue2 = analogRead(sensorPin2);
  // Map the sensor value to a percentage (0% - 100%)
  percentMoisture1 = map(sensorValue1, dryValue, wetValue, 0, 100);
  percentMoisture2 = map(sensorValue2, dryValue, wetValue, 0, 100);
  // Ensure the moisture percentage is within valid range (0-100%)
  percentMoisture1 = constrain(percentMoisture1, 0, 100);
  percentMoisture2 = constrain(percentMoisture2, 0, 100);
  float humidity = dht.readHumidity();
  // Read temperature as Celsius (default)
  float temperature = dht.readTemperature();
  float heatIndexC = dht.computeHeatIndex(temperature, humidity, false);

  // Check if any reads failed and exit early (to try again).
  /*if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;}*/
  // Print the sensor value and moisture percentage to the serial monitor
  //Serial.print("\n");
  //Serial.print("Sensor1 Value: ");
  Serial.print(sensorValue1);
   Serial.print(" ");
  //Serial.print("  Moisture: ");
  Serial.print(percentMoisture1);  
  Serial.print(" ");
  //Serial.print("\nSensor2 Value: ");
 Serial.print(sensorValue2);
  Serial.print(" ");
  //Serial.print("  Moisture: ");
 Serial.print(percentMoisture2);
  Serial.print(" ");
  //Serial.println("%");
  //Serial.print("\n");
  // Compute heat index in Celsius
  //Serial.print("Humidity: ");
  Serial.print(humidity);
   Serial.print(" ");
  //Serial.print(" %\t");
  //Serial.print("Temperature: ");
  Serial.print(temperature);
   Serial.print(" ");
  //Serial.print(" °C ");
 // Serial.print("Heat index: ");
  Serial.print(heatIndexC);
   Serial.print(" ");
  Serial.println();
  //Serial.print(" °C ");
  delay(500);
}