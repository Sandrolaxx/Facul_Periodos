#include "TimerOne.h"

#define LED1 5

#define BTN1 3

bool isLigado = true;
bool isExecutando = false;

void onInterrupt() {
  Serial.println("TEste2");

  if (isExecutando) {
    // Timer1.stop();
    Serial.println("TEste");
  }

}

void setup() {
  Serial.begin(9600);
  pinMode(LED1, OUTPUT);
  pinMode(BTN1, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(BTN1), onInterrupt, CHANGE);
  // Timer1.attachInterrupt(handleTurn);

  // Timer1.initialize(1000000);
  // Timer1.start();
}

void loop() {
  delay(100);

  isExecutando = true;
}

void handleTurn() {
  if(isLigado) {
    digitalWrite(LED1, LOW);
  } else {
    digitalWrite(LED1, HIGH);
  }

  isLigado = !isLigado;
}