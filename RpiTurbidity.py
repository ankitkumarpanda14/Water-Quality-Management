import time
import urllib as url
import serial

ArduinoSerial=serial.Serial("/dev/ttyACM0",9600)
time.sleep(2)

while True:
  s=ArduinoSerial.readline()
  print s
  temp=url.urlopen("https://api.thingspeak.com/update?api_key=RWDYNAB8A0Z2W941&field1="+str(s))
  time.sleep(15)
  s1=ArduinoSerial.readline()
  print s1
  temp=url.urlopen("https://api.thingspeak.com/update?api_key=RWDYNAB8A0Z2W941&field2="+str(s1))
  time.sleep(15)
 
