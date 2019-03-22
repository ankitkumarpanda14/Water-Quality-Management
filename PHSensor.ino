#define SensorPin A0            
#define samplingInterval 20
#define printInterval 800
#define ArrayLenth  40    
int pHArray[ArrayLenth];  
int pHArrayIndex=0;    
void setup()
{
  Serial.begin(9600);  
}
void loop()
{
  static unsigned long samplingTime = millis();
  static unsigned long printTime = millis();
  static float pHValue,voltage;
  if(millis()-samplingTime > samplingInterval)
  {
      pHArray[pHArrayIndex++]=analogRead(SensorPin);
      if(pHArrayIndex==ArrayLenth)
      {
        pHArrayIndex=0;
      }
      voltage = avergearray(pHArray, ArrayLenth)*5.0/1024;
      
      pHValue = 3.5*voltage;
      
      samplingTime=millis();
  }
  if(millis() - printTime > printInterval)  
  {
    Serial.print("pH value:");
    Serial.println(pHValue,2);
    printTime=millis();
  }
}
double avergearray(int* arr, int number)
{
  int i;
  int max,min;
  double avg;
  long amount=0;
  if(number<5)
  {  
    for(i=0;i<number;i++){
      amount+=arr[i];
    }
    avg = amount/number;
    return avg;
  }
  else
  {
    if(arr[0]<arr[1])
    {
      min = arr[0];max=arr[1];
    }
    else
    {
      min=arr[1];max=arr[0];
    }
    for(i=2;i<number;i++)
    {
      if(arr[i]<min)
      {
        amount+=min;        //arr<min
        min=arr[i];
      }
      else {
        if(arr[i]>max)
        {
          amount+=max;    //arr>max
          max=arr[i];
        }
        else
        {
          amount+=arr[i]; //min<=arr<=max
        }
      }
    }
    avg = (double)amount/(number-2);
  }
  return avg;
}
