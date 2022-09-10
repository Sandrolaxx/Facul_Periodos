#define BTN1 2
#define BTN2 3
#define LED1 6
#define LED2 5

#define LED_RGB_RED 11
#define LED_RGB_GREEN 10
#define LED_RGB_BLUE 9

#define SONAR_TRIG 7
#define SONAR_ECHO 8

#define LDR A1
#define TEMP A0

#define INFRA_VERMELHO A2

int distance;
long duration;
long luminosity;
long tensaoSaida;
long temperaturaC;
long sensorTemperature;
long sensorInfra;

boolean isSystemOn;
boolean isRompido = false;

String color = "BLUE";

void setup() {
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  Serial.begin(9600);
  pinMode(BTN1, INPUT);

  pinMode(SONAR_TRIG, OUTPUT);
  pinMode(SONAR_ECHO, INPUT);

  pinMode(LED_RGB_RED, OUTPUT);
  pinMode(LED_RGB_GREEN, OUTPUT);
  pinMode(LED_RGB_BLUE, OUTPUT);
}

void loop() {
  verifySystemStatus();
  
  if (isSystemOn) {
    delay(100);

    luminosity = analogRead(LDR);
    sensorInfra = analogRead(INFRA_VERMELHO);
    distance = calculateDistance();
    temperaturaC = calcularTemperatura();

    Serial.print(",");
    Serial.print(temperaturaC);
//    Serial.print(",");
//    Serial.print(luminosity);
    
    if (distance < 40) {
      digitalWrite(LED1, HIGH);
    } else {
      digitalWrite(LED1, LOW);
    }

    if (temperaturaC > 26 
      && luminosity > 600) {
        digitalWrite(LED2, HIGH);
    } else {
        digitalWrite(LED2, LOW);
    }

    if (isBarreiraRompida()) {
      checkColor();
    }
    
  } else {
    digitalWrite(LED1, LOW);
    digitalWrite(LED2, LOW);
    RGB_color(0,0,0);
  }

}

boolean isBarreiraRompida() {
  return sensorInfra == 0;
}

void checkColor() {
  
  if(color == "BLUE" && !isRompido) {
    RGB_color(0,0,255);

    color = "GREEN";

    isRompido = true;
    return;
  }

  if(color == "GREEN" && !isRompido) {
    RGB_color(0,255,0);

    color = "RED";

    isRompido = true;
    return;
  }
  
  if(color == "RED" && !isRompido) {
    RGB_color(255,0,0);

    color = "BLUE";

    isRompido = true;
    return;
  }

  delay(200);
  isRompido = false;
  
}

bool verifySystemStatus() {
  if (digitalRead(BTN1) == LOW) {
    delay(100);
    isSystemOn = !isSystemOn;
  }

   if (digitalRead(BTN2) == LOW) {
    delay(100);
    isSystemOn = false;
  }

  while(digitalRead(BTN1) == LOW && digitalRead(BTN2) == LOW ) {
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
  }
  
}

long calcularTemperatura() {
    sensorTemperature = analogRead(TEMP);
    tensaoSaida = (sensorTemperature * 5000) / 1024; 
    
    return tensaoSaida / 10; 
}

void RGB_color(int red_light_value, int green_light_value, int blue_light_value) {
  analogWrite(LED_RGB_RED, red_light_value);
  analogWrite(LED_RGB_GREEN, green_light_value);
  analogWrite(LED_RGB_BLUE, blue_light_value);
}

int calculateDistance(){ 
  
  digitalWrite(SONAR_TRIG, LOW); 
  delayMicroseconds(2);
  
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(SONAR_TRIG, HIGH); 
  
  delayMicroseconds(10);
  
  digitalWrite(SONAR_TRIG, LOW);
  
  //Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(SONAR_ECHO, HIGH);
  
  distance= duration*0.034/2;
  
  return distance;
}