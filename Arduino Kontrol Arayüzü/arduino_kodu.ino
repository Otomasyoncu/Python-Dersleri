#include <SoftwareSerial.h>

String gelen;

void setup() {
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(1,OUTPUT);
  pinMode(0,OUTPUT);
  

}

void loop() {
  gelen = Serial.read();
  if (gelen == "65")
      {
        digitalWrite(13,1);
        }
  if (gelen == "66")
  {  
    digitalWrite(13,0);
      
    }
  if (gelen =="99")
  {
    digitalWrite(12,1);
   
    
    }
if (gelen == "100")
   {
    digitalWrite(12,0);
    }
if (gelen == "101")

{
  digitalWrite(11,1);
  }
if (gelen == "102")
{
  digitalWrite(11,0);
  
  }
if (gelen == "103")
{
  digitalWrite(10,1);
  }

  if (gelen == "104")
{
  digitalWrite(10,0);
  }
if (gelen == "105")
{
  digitalWrite(9,1);
  }
if (gelen == "106")
{
  digitalWrite(9,0);
  }
if (gelen == "107")
{
  digitalWrite(8,1);
  }
if (gelen == "108")
{
  digitalWrite(8,0);
  }
if (gelen == "109")
{
  digitalWrite(7,1);
  }
if (gelen == "110")
{
  digitalWrite(7,0);
  }
if (gelen == "111")
{
  digitalWrite(6,1);
  }
if (gelen == "112")
{
  digitalWrite(6,0);
  }
if (gelen == "113")
{
  digitalWrite(5,1);
  }
if (gelen == "114")
{
  digitalWrite(5,0);
  }
if (gelen == "115")
{
  digitalWrite(4,1);
  }
if (gelen == "116")
{
  digitalWrite(4,0);
  }
if (gelen == "117")
{
  digitalWrite(3,1);
  }
if (gelen == "118")
{
  digitalWrite(3,0);
  }
if (gelen == "119")
{
  digitalWrite(2,1);
  }
if (gelen == "120")
{
  digitalWrite(2,0);
  }
if (gelen == "121")
{
  digitalWrite(1,1);
  }
if (gelen == "122")
{
  digitalWrite(1,0);
  }
if (gelen == "74")
{
  digitalWrite(0,1);
  }
if (gelen == "75")
{
  digitalWrite(0,0);
  }
if (gelen =="82")
{
  digitalWrite(0,0);
  digitalWrite(1,0);
  digitalWrite(2,0);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  digitalWrite(6,0);
  digitalWrite(7,0);
  digitalWrite(8,0);
  digitalWrite(9,0);
  digitalWrite(10,0);
  digitalWrite(11,0);
  digitalWrite(12,0);
  digitalWrite(13,0);
  
  
  
  }

}
