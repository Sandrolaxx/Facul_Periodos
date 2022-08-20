#define LED0 5
#define LED1 6
#define BOTAO 2
int clicks = 0;
boolean isSystemOn = false;

void setup() {
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  Serial.begin(9600);
  pinMode(BOTAO, INPUT);
}

void handleTurnLED0(bool on) {
  digitalWrite(LED0, on ? HIGH : LOW);
}

void handleTurnLED1(bool on) {
  digitalWrite(LED1, on ? LOW : HIGH);
}

void loop() {
  int pototentiometerValue = analogRead(A0);
  boolean isPototentiometerOnRange = ((pototentiometerValue > 100
          && pototentiometerValue < 300)
           || (pototentiometerValue > 800
             && pototentiometerValue < 1000));
  delay(100);
  
  while(digitalRead(BOTAO) == LOW) {
    if (digitalRead(BOTAO) == LOW) {
      isSystemOn = true;
      handleTurnLED0(true);
    } else {
      isSystemOn = false;
      handleTurnLED0(false);
    }
  }

  if (isSystemOn) {
    if(!isPototentiometerOnRange) {
      handleTurnLED1(true); 
    }
    else {
      handleTurnLED1(false); 
    }
    
  }
   
}
