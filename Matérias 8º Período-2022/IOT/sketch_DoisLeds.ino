#define LED0 2
#define LED1 4

void setup() {
  // put your setup code here, to run once:
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
}

void handleTurn(bool on, bool changeAll) {
  if(changeAll) {
    digitalWrite(LED0, on ? HIGH : LOW);
    digitalWrite(LED1, on ? HIGH : LOW);
  } else {
    digitalWrite(LED0, on ? HIGH : LOW);
    digitalWrite(LED1, !on ? HIGH : LOW);
  }

  delay(500);
}

void loop() {
  // put your main code here, to run repeatedly:
  handleTurn(true, true);
  handleTurn(false, false);
  handleTurn(true, false);
  handleTurn(false, true);
}