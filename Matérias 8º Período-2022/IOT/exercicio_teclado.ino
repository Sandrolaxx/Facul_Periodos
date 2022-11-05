String pressedValue;

void setup() {
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);

  pinMode(12, OUTPUT);
  
  Serial.begin(9600);
}
 
void loop() {
    digitalWrite(12, HIGH);
  
    for (int ti = 3; ti<7; ti++) {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    digitalWrite(ti, HIGH);

    //Verifica se alguma tecla da coluna 1 foi pressionada
    if (digitalRead(8) == HIGH) {
      pressedValue += getKeyboardNumber(ti-2, 1); 
      while(digitalRead(8) == HIGH){}
    }
 
    //Verifica se alguma tecla da coluna 2 foi pressionada    
    if (digitalRead(9) == HIGH) {
      pressedValue += getKeyboardNumber(ti-2, 2); 
      while(digitalRead(9) == HIGH){};
    }
     
    //Verifica se alguma tecla da coluna 3 foi pressionada
    if (digitalRead(10) == HIGH) {
      pressedValue += getKeyboardNumber(ti-2, 3);
      while(digitalRead(10) == HIGH){}
    }
     
    //Verifica se alguma tecla da coluna 4 foi pressionada
    if (digitalRead(11) == HIGH) {
      if (getKeyboardNumber(ti-2, 4) == "*") {
        Serial.print(pressedValue);
        pressedValue = "";
      } else {
        pressedValue += getKeyboardNumber(ti-2, 4);
      }
      while(digitalRead(11) == HIGH){} 
    }
   }
   
   delay(10);
}
 
String getKeyboardNumber(int linha, int coluna) {     
      if(linha == 1 && coluna == 4) {
        return "1";
      }

      if (linha == 2 && coluna == 4) {
        return "4";
      }

      if (linha == 3 && coluna == 4) {
        return "7";
      }

      if (linha == 4 && coluna == 4) {
        return "*";
      }

      if (linha == 1 && coluna == 3) {
        return "2";
      }

      if (linha == 2 && coluna == 3) {
        return "5";
      }

      if (linha == 3 && coluna == 3) {
        return "8";
      }

      if (linha == 4 && coluna == 3) {
        return "0";
      }

      if (linha == 1 && coluna == 2) {
        return "3";
      }

      if (linha == 2 && coluna == 2) {
        return "6";
      }

      if (linha == 3 && coluna == 2) {
        return "9";
      }

      if (linha == 4 && coluna == 2) {
        return "#";
      }
      
      if (linha == 1 && coluna == 1) {
        return "A";
      }

      if (linha == 2 && coluna == 1) {
        return "B";
      }

      if (linha == 3 && coluna == 1) {
        return "C";
      }

      if (linha == 4 && coluna == 1) {
        return "D";
      }
}
