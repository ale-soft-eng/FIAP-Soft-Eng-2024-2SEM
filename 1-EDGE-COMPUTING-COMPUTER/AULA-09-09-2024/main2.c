#include<ArduinoJson.h>
#include<DHT.h>

#define DHTPIN 7
#define DHTTYPE 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
dht.begin();
Serial.begin(9600);
}

void loop() {
StaticJsonDocument<50>json;


float temp  = dht.readTemperature();
float umi = dht.readHumidity();

json["temperatura"] = temp;

json["umidade"] = umi;

serializeJson(json, Serial);
Serial.println();
delay(1000);

}
