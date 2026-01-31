int count=0, x=0, y=0, z=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.print("Hello, world! Publishing: ");
  //Serial.println(count);
  //count++;
  x+=1;
  y+=2;
  z+=3;
  Serial.print(x);  Serial.print(",");
  Serial.print(y);  Serial.print(",");
  Serial.println(z);
  delay(1000);
}
