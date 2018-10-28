//PB: servo doesn't covert 360degs -> to solve later use this for now X)
#include <Servo.h>

Servo azimut_motor;
Servo altitude_motor;

bool laser = false;

// Maximum number of substrings expected
const int MAX_SUBSTRINGS = 4;


void getValues(char* s, char** substrings) {
    //Serial.println(s);
    // First clear the array of substrings
    for (int i = 0; i < MAX_SUBSTRINGS; i++)
        substrings[i] = 0;
    // Now split the input string
    char* text = strtok(s,":");
    //Serial.println(text);
    //Serial.println(s);
    int i = 0;
    while (text != 0 && i < MAX_SUBSTRINGS) {
      
    //Serial.println(text);
        // A token was found: append it to the array of substrings
        substrings[i++] = text;
        text = strtok(NULL,":");
    //Serial.println(s);
        Serial.println(text);
    }
}



/**
 * Read a float and send back a "c" to say it's over and read
 */
float readFloat(){
  float value=Serial.parseFloat();   
  Serial.print("Float");                    //Print out nicely formatted output.
  Serial.print(value); 
  Serial.write("c");
  return value;
}

/**
 * Point a the star *_*
 */
bool setMotors(float azimut, float altitude){
  //Serial.write((int)azimut*1000);
  //Serial.write("m\n");
  azimut = azimut + 90;
  if(azimut >= 360){
    azimut = azimut - 360;
  }
  azimut_motor.write(azimut);                  // sets the servo position according to the scaled value
  altitude_motor.write(altitude + 90); // sets the servo position according to the scaled value
  Serial.println(azimut);  
  delay(1000);
  //Serial.println("DONE");  
}
 
void setup() {
  Serial.begin(9600);      // turn on Serial Port
  azimut_motor.attach(9);  // attaches the servo on pin 9 to the servo object
  altitude_motor.attach(10);  // attaches the servo on pin 10 to the servo object
  
altitude_motor.write(90);
azimut_motor.write(90);
}


void setMotors(){
   float azimut = 0;
    float altitude = 0;
    //double az_checked = false;
    //double alt_checked = false;
  
    //Set alt and azimut
   // while(az_checked == false && alt_checked == false){
   //   Serial.write("r");
   //   String type=Serial.readString();
   //   if(type == "az"){
   //     azimut = readFloat();
   //     az_checked = true;
   //   }
   //   if(type == "alt"){
   //     altitude = readFloat();
   //     alt_checked = true;
   //   }
      
      //String values=Serial.readString(); 
      //Serial.println(values);  
      String values = "az:0:alt:-90";
      
      char charBuf[values.length()+1];
      values.toCharArray(charBuf, values.length()+1);
      
      char* substrings[MAX_SUBSTRINGS];
      getValues(charBuf, substrings);
      azimut = atof(substrings[1]);
      altitude = atof(substrings[3]);
      
      //az_checked = true;
      //alt_checked = true;
   
    //}
    
    setMotors(azimut, altitude);
}
 
void loop() {

  while (!Serial.available()) {} // wait for data to arrive
  

  if(Serial.available() > 0){
    //Turn on the laser or off the laser
    laser = !laser;
    setMotors();

  }
  Serial.write("s\n");
 
}
