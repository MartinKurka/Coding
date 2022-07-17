#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include "DHT.h"

// Uncomment one of the lines below for whatever DHT sensor type you're using!
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT21   // DHT 21 (AM2301)
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

// Dallas DS18b20
#include <DallasTemperature.h>
#include <OneWire.h>
#define ONE_WIRE_BUS 5
OneWire oneWire(ONE_WIRE_BUS); 
DallasTemperature sensors(&oneWire);            // Pass the oneWire reference to Dallas Temperature.

/*Put your SSID & Password*/
const char* ssid = "SPARTA";  // Enter SSID here
const char* password = "9306111078";  //Enter Password here

ESP8266WebServer server(80);
IPAddress ip(192,168,0,20); 
IPAddress gateway(192,168,0,1); 
IPAddress subnet(255,255,255,0); 

// DHT Sensor
uint8_t DHTPin = 2; 
DHT dht(DHTPin, DHTTYPE);
float Temperature;
float Humidity;
 
void setup() {
  Serial.begin(115200);
  delay(100);  
  pinMode(DHTPin, INPUT);
  dht.begin();              

  Serial.println("Connecting to ");
  Serial.println(ssid);

  //connect to your local wi-fi network
  //WiFi.begin(ssid, password);
  WiFi.config(ip,gateway,subnet);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  
  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");  
  Serial.println(WiFi.localIP());

  server.on("/", handle_OnConnect);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("HTTP server started");

  sensors.begin();
//  sensors.setResolution(0, 11);                 // adresa senzoru a kolik bit přesnost (9 - 12)
//  sensors.requestTemperatures();                // Send the command to get temperatures  
//  Serial.println("Temperature is: ");
//  Serial.println(sensors.getTempCByIndex(0));   // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire

}
void loop() {
  
  server.handleClient();
  
}

float dallas_temp() {
  float temp = 0;
  sensors.requestTemperatures();                // Send the command to get temperatures  
//  Serial.println("Temperature is: ");
//  Serial.println(sensors.getTempCByIndex(0));   // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire
  temp = sensors.getTempCByIndex(0);
  return temp;
}

void handle_OnConnect() {

  Temperature = dallas_temp(); // Gets the values of the temperature
//  Temperature = dht.readTemperature(); // Gets the values of the temperature
  Humidity = dht.readHumidity(); // Gets the values of the humidity 
  server.send(200, "text/html", SendHTML(Temperature,Humidity)); 
}

void handle_NotFound(){
  server.send(404, "text/plain", "Not found");
}

String SendHTML(float Temperaturestat,float Humiditystat){
  String ptr = "<!DOCTYPE html> <html>\n";
  ptr +="<head><meta charset=\"UTF-8\" name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
  ptr +="<title>ESP8266 Weather Report</title>\n";
  ptr +="<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
  ptr +="body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
  ptr +="p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
  ptr +="</style>\n";
  ptr +="</head>\n";
  ptr +="<body>\n";
  ptr +="<div id=\"webpage\">\n";
  ptr +="<h1>ESP8266 NodeMCU Weather Report</h1>\n";
  
  ptr +="<p>Temperature</p>";
  ptr +="<p>";
  ptr +=(float)Temperaturestat;
  ptr +="</p>";
  ptr +="<p>Humidity";
  ptr +="<p>";
  ptr +=(int)Humiditystat;
  ptr +="</p>";
  
  ptr +="</div>\n";
  ptr +="</body>\n";
  ptr +="</html>\n";
  return ptr;
}
