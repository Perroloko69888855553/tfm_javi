int selector =1;
int TriggerPin;
int EchoPin;

void setup() {
  Serial.begin(9600);
 // Serial.println("Pro_Javi");
  selector =1;
  delay(2000);
   int selector =1;
  int TriggerPin = 1;
  
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
  pinMode(5, OUTPUT);
  pinMode(6, INPUT);
  pinMode(7, OUTPUT);
  pinMode(8, INPUT);
  pinMode(9, OUTPUT);
  pinMode(10, INPUT);
  pinMode(11, OUTPUT);
  pinMode(12, INPUT);
  pinMode(13, OUTPUT);
  pinMode(14, INPUT);
  pinMode(15, OUTPUT);
  pinMode(16, INPUT);
  pinMode(17, OUTPUT);
  pinMode(18, INPUT);
  pinMode(19, OUTPUT);
  
}

void loop() {
  if( selector > 9 ) selector =1;
  if(selector == 9 )selector =10;
 //selector =4;
  EchoPin = selector * 2;
  TriggerPin = EchoPin +1;
   int cm = ping(TriggerPin, EchoPin);
   if(selector == 10) selector = 9;
   byte identificador = selector <<3;
   //Serial.print(selector);
  //  Serial.print("...");
 //   Serial.println(cm);

   byte Distancia = cm | 0x80; //& 0x7F;
   cm= cm>> 7;
  identificador = identificador | (0x07 & cm);
  Serial.write(identificador);
  Serial.write(Distancia);
    
  delay(500);
   selector++;
}

int ping(int TriggerPin, int EchoPin) {
   unsigned long distanceCm;
   unsigned long tMaxDistancia =24000;
   long tDistancia;
   digitalWrite(TriggerPin, LOW);  //para generar un pulso limpio ponemos a LOW 4us
   delayMicroseconds(4);
   digitalWrite(TriggerPin, HIGH);  //generamos Trigger (disparo) de 10us
   delayMicroseconds(10);
   digitalWrite(TriggerPin, LOW);
   tDistancia = pulseIn(EchoPin, HIGH, tMaxDistancia);
   if (tDistancia ==0) tDistancia = tMaxDistancia;
   distanceCm = (340 * tDistancia) / 20000;
    return distanceCm;
}
