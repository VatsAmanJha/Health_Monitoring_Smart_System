#include <WiFi.h>
#include <FirebaseESP32.h>

const int MAX_LINES = 10;         // Maximum number of lines to store
String receivedLines[MAX_LINES];  // Array to store received lines
int lineCount = 0;                // Counter for the number of lines received

#define FIREBASE_HOST "https://fir-386c7-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "AIzaSyA1Mb6EFLCsD4JV1EC2q67bV2Z7hqvb4kk"
#define WIFI_SSID "jai shree ram"
#define WIFI_PASSWORD "Vimdhayakji"


//Define FirebaseESP32 data object
FirebaseData firebaseData;
FirebaseJson json;

void setup() {
  Serial.begin(9600);     // Initialize Serial Monitor at 9600 baud rate
  Serial1.begin(115200);  // Initialize another Serial port at 115200 baud rate

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
  }

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  Serial.println("------------------------------------");
  Serial.println("Connected...");
}

void loop() {
  if (Serial.available()) {
    if (lineCount < MAX_LINES) {
      // Read data from Arduino
      String receivedData = Serial.readStringUntil('\n');
      receivedLines[lineCount] = receivedData;
      lineCount++;
    } else {
      // Array is full, print the stored lines and reset
      Serial.println("Array is full. Printing stored lines:");
      for (int i = 0; i < lineCount; i++) {
        Serial.print("Line ");
        Serial.print(i + 1);
        Serial.print(": ");
        Serial.println(receivedLines[i]);
      }
      // Send data to Firebase
      json.set("/SoundLevel", receivedLines[0]);
      json.set("/HeartRate", receivedLines[1]);
      json.set("/SpO2", receivedLines[2]);
      json.set("/AirQuality", receivedLines[3]);
      json.set("/Humidity", receivedLines[4]);
      json.set("/Temperature", receivedLines[5]);
      json.set("/AmbientC", receivedLines[6]);
      json.set("/ObjectC", receivedLines[7]);
      json.set("/AmbientF", receivedLines[8]);
      json.set("/ObjectF", receivedLines[9]);
      Firebase.updateNode(firebaseData, "/Data", json);
      Serial.print("Data sent to Firebase: ");
      lineCount = 0;
      memset(receivedLines, 0, sizeof(receivedLines));
    }
  }
  if (Serial1.available()) {
    if (lineCount < MAX_LINES) {
      // Read data from Arduino
      String receivedData = Serial.readStringUntil('\n');
      receivedLines[lineCount] = receivedData;
      lineCount++;
    }

    // Send data received from one Serial port to the other
    // Serial.println("Received from Serial1: " + dataToSerial);
  }
}
