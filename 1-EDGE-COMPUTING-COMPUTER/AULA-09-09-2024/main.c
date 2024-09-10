#include<ArduinoJson.h>
#include<DHT.h>

#define DHTPIN 7
#define DHTTYPE 11

DHT dht(DHTPIN, DHTTYPE)

int trigger = 7;
int echo = 8;
int dist = 0;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo INPUT);
  Serial.begin(9600);// put your setup code here, to run once:
}

void loop() {
  digitalWrite(trigger, LOW);
  delayMicroseconds(5);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);

  dist = pulseIn(echo, HIGH);
  dist = dist / 58;

  //Aloca bufer para o objeto json
  StaticJsonDocument<50>json;

  json["distancia"] = dist;

  serializeJson(json, Serial);
  Serial.println("distancia");
  delay(1000);

}
