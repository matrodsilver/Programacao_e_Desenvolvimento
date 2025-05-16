#include <Arduino.h>
#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to enable it
#endif

BluetoothSerial SerialBT;

void setup() {
    pinMode(2, OUTPUT);
    Serial.begin(9600);  // For debug messages
    SerialBT.begin("ESP32_BT"); // Bluetooth device name
    Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
    // If data is coming from Bluetooth Serial
    if (SerialBT.available()) {
        digitalWrite(2, HIGH); // Turn on LED
        String data = SerialBT.readStringUntil('\n');
        Serial.print("Received via BT: ");
        Serial.println(data);
        // Echo back to mobile device
        SerialBT.println("ESP32 received: " + data);
    }
    
    digitalWrite(2, LOW); // Turn off LED when no data
    delay(20); // Small delay to prevent busy waiting
}