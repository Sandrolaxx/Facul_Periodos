#define LED0 5

void setup() {
  pinMode(LED0, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  int potentiometerValue = analogRead(A0);
  long result = potentiometerValue / 4;

  Serial.println(potentiometerValue);
  Serial.println(result); 
  delay(100);
  analogWrite(A0, result);
}
