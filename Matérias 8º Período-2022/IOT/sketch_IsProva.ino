#define ESTEIRA 6
#define FRESADORA 5

#define TECLA_1 2
#define TECLA_2 3

#define SONAR_TRIG 7
#define SONAR_ECHO 8

#define TEMP A0
#define INFRA_VERMELHO A2

int distance;
long duration;
long sensorInfra;
long tensaoSaida;
long temperaturaC;
long sensorTemperature;
boolean isRompido = false;
boolean isExecuteAgain = true;

void setup() {
  pinMode(ESTEIRA, OUTPUT);
  pinMode(FRESADORA, OUTPUT);

  pinMode(TECLA_1, INPUT);
  pinMode(TECLA_2, INPUT);

  pinMode(SONAR_TRIG, OUTPUT);
  pinMode(SONAR_ECHO, INPUT);

  Serial.begin(9600);
}


bool validation = false;
bool validation_2 = false;
bool validation_3 = false;
bool validation_4 = false;
void loop() {
  distance = calculateDistance();
  Serial.print(",");
  Serial.print(distance);
  delay(200);
  bool isApertadoTecla1 = digitalRead(TECLA_1) == LOW;
  
  if (isApertadoTecla1 || validation) {
      validation = true;
      if (validation_2) {
        digitalWrite(ESTEIRA, LOW);
      } else{
        digitalWrite(ESTEIRA, HIGH);  
      }
      
      sensorInfra = analogRead(INFRA_VERMELHO);
  
      if (isBarreiraRompida() || validation_2) {
        validation_2 = true;
        if (validation_3){
          digitalWrite(ESTEIRA, LOW);  
        } else {
          digitalWrite(FRESADORA, HIGH);  
        }
  
        temperaturaC = calcularTemperatura();

      
  
        if (temperaturaC >= 24 || validation_3) {
          validation_3 = true;
          if (!validation_4) {
            digitalWrite(FRESADORA, LOW);  
          }
          bool isApertadoTecla2 = digitalRead(TECLA_2) == LOW;
  
          if (isApertadoTecla2 || validation_4) {
            validation_4 = true;
            digitalWrite(ESTEIRA, HIGH);
            distance = calculateDistance();

            
            delay(200);
            if (distance <= 5) {
              digitalWrite(ESTEIRA, LOW);

              validation_2 = false;
              validation = false;
              validation_4 = false;
              validation_3 = false;
            } 
          } 
       
      }
    }
  }
}

long calcularTemperatura() {
    sensorTemperature = analogRead(TEMP);
    tensaoSaida = (sensorTemperature * 5000) / 1024; 
    
    return tensaoSaida / 10; 
}


int calculateDistance(){ 
  
  digitalWrite(SONAR_TRIG, LOW); 
  delayMicroseconds(2);
  
  digitalWrite(SONAR_TRIG, HIGH); 
  
  delayMicroseconds(10);
  
  digitalWrite(SONAR_TRIG, LOW);
  
  duration = pulseIn(SONAR_ECHO, HIGH);
  
  distance = duration*0.034/2;
  
  return distance;
}

boolean isBarreiraRompida() {
  return sensorInfra == 0;
}