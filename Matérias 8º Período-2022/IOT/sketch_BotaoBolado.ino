#define LED0 0
#define BOTAO 1
int clicks = 0;

void setup() {
  pinMode(LED0, OUTPUT);
  pinMode(BOTAO, INPUT);
}

void handleTurn(bool on) {
  digitalWrite(LED0, on ? HIGH : LOW);
}

void loop() {
  if(digitalRead(BOTAO) == LOW) {
    while(digitalRead(BOTAO) == LOW);
    
    clicks++;
    
    Serial.print("Clicks: " + int(clicks));
      
    if(clicks == 3) {
      handleTurn(true);
    }
  }

  if(clicks == 6) { 
    handleTurn(false);
    clicks = 0;
  }
}