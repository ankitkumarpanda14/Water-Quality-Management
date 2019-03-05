int Tpin = A0;
float volt;
float ntu;

void setup()
{
    Serial.begin(9600);

}

void loop()
{
  volt= 0;
  for(int i=0;i<200;i++)
  {
    volt+= (((float)analogRead(Tpin)*5)/1023);
  }
  volt = volt/200;
  volt = round_to_dp(volt,1);
  if(volt<2.5)
  {
    ntu = 3000;
  }
  else
  {
  ntu = -1120.4*square(volt)+5742.3*volt-4353.1;
  }
  Serial.print(volt);
  Serial.println("V");
  Serial.print(ntu);
  Serial.println("NTU");
  delay(1000);  
}

float round_to_dp( float in_value, int decimal_place )
{
  float multiplier = powf( 10.0f, decimal_place );
  in_value = roundf( in_value * multiplier ) / multiplier;
  return in_value;
}
