#include <SPI.h>
#include <SD.h>

File myFile;

int chipsel = 4;

//variables to read data from tubes
int val1, val2, val3;
unsigned long timestamp;

int sen1 = A0;
int sen2 = A1;
int sen3 = A2;

void setup() {                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
  // initalize ss pin , 10
  pinMode(chipsel, OUTPUT);

  //set up input pins for 3 capacitor pairs
  pinMode(sen1, INPUT);
  pinMode(sen2, INPUT);
  pinMode(sen3, INPUT);

  digitalWrite(chipsel, HIGH);

  pinMode(10, OUTPUT);
  digitalWrite(10, HIGH);

  Serial.begin(9600);

  if (!SD.begin(chipsel)) {
      while(1);
      Serial.println("not initialized SD");
  }
}

void loop() {
  //debugging message
  Serial.print("within loop ");

  //take reading from each capacitor pair
  val1 = analogRead(sen1);
  val2 = analogRead(sen2);
  val3 = analogRead(sen3);

  //open file for writing
  File dataFile = SD.open("sen3.txt", FILE_WRITE);

  //debugging message to see measured values
  Serial.print(val1);
  Serial.print(",");
  Serial.print(val2);
  Serial.print(",");
  Serial.println(val3);

 //write measured values to file in csv format
  if (dataFile) {
    timestamp = millis();
    dataFile.print(timestamp);
    dataFile.print(",");
    dataFile.print(val1);
    dataFile.print(",");
    dataFile.print(val2);
    dataFile.print(",");
    dataFile.println(val3);
    dataFile.close();
    Serial.println("w");
  }

  //short delay to allow SD card library to finish its tasks
  //50ms was selected based on the oscilloscope readings we took
  //it should be frequent enough to take more than one reading during the up-down pattern
  //making it recognizable in the readings from the csv
  delay (50);

}
