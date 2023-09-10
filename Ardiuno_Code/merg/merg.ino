#include <Wire.h>
#include "MAX30100_PulseOximeter.h"
#include <DHT.h>
#include <Adafruit_MLX90614.h>

const int soundSensorPin = A0; // Analog pin for the sound sensor
float threshold = 72.5; // Adjust this threshold based on your sensor's sensitivity

#define REPORTING_PERIOD_MS 1000
#define DHTPIN 2
#define DHTTYPE DHT22

PulseOximeter pox;
int sensorPin = A4;
int sensorData;
DHT dht(DHTPIN, DHTTYPE);
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

uint32_t tsLastReport = 0; // Declaration of tsLastReport

void onBeatDetected() {
    Serial.println("Beat!");
}

void setup() {
    Serial.begin(9600);
    Serial.println("Initializing pulse oximeter..");

    if (!pox.begin()) {
        Serial.println("FAILED");
        for (;;);
    } else {
        Serial.println("SUCCESS");
    }

    pox.setIRLedCurrent(MAX30100_LED_CURR_7_6MA);
    pox.setOnBeatDetectedCallback(onBeatDetected);

    pinMode(sensorPin, INPUT);

    dht.begin();

    Serial.println("Arduino MLX90614 Testing");
    mlx.begin();
}

void loop() {
    pox.update();

    int soundValue = analogRead(soundSensorPin);

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    float mlxAmbientC = mlx.readAmbientTempC();
    float mlxObjectC = mlx.readObjectTempC();
    float mlxAmbientF = mlx.readAmbientTempF();
    float mlxObjectF = mlx.readObjectTempF();

    sensorData = analogRead(sensorPin);

    if (millis() - tsLastReport > REPORTING_PERIOD_MS) {
        Serial.print("Sound Level: ");
        Serial.println(soundValue);

        Serial.print("Heart rate:");
        Serial.print(pox.getHeartRate());
        Serial.print("bpm / SpO2:");
        Serial.print(pox.getSpO2());
        Serial.println("%");

        Serial.print("Air Quality:");
        Serial.print(sensorData, DEC);
        Serial.println(" PPM");

        Serial.print("Humidity: ");
        Serial.print(humidity);
        Serial.print(" %\t");
        Serial.print("Temperature: ");
        Serial.print(temperature);
        Serial.println(" °C");

        Serial.print("Ambient = "); 
        Serial.print(mlxAmbientC);
        Serial.print("*C\tObject = ");
        Serial.print(mlxObjectC);
        Serial.println("*C");
        Serial.print("Ambient = ");
        Serial.print(mlxAmbientF);
        Serial.print("*F\tObject = ");
        Serial.print(mlxObjectF);
        Serial.println("*F");

        tsLastReport = millis();
    }

    delay(5000);
}
