int Taster=2; //Deklaration
  int tasterstatus=0;// Variabel in der Intreger gespeichert werden
  int ROTA=13;
  int GELB=12;
  int GRUENA=8;
  int ROT=7;
  int GRUEN=4;

void setup() {
  Serial.begin(9600);//setzen der baudrate
  pinMode(2, INPUT); //pin2 input = Eingang
  pinMode(13, OUTPUT);// pin13 output = Ausgang
  pinMode(12, OUTPUT);// pin12 output = Ausgang
  pinMode(8, OUTPUT);// pin8 output = Ausgang
  pinMode(7, OUTPUT);// pin4 output = Ausgang
  pinMode(4, OUTPUT);// pin7 output = Ausgang
}

void loop() {
digitalWrite(GRUENA, HIGH);//Schaltet pin8 ein
digitalWrite(ROT,HIGH);
int tasterstatus;// Variabel in der Intreger gespeichert werden
tasterstatus = digitalRead(Taster);// Auslesen von pin 2(Befehl: digitalRead)
Serial.println(tasterstatus,DEC);// gibt den gelesenen input in dezimalzahl wieder
if (tasterstatus == HIGH)//begin der if-loop
  {
  delay(2000);// wartezeit 2sek
  digitalWrite(GRUENA,LOW);//Schaltet pin8 aus
  delay(2000);
  digitalWrite(GELB,HIGH);
  delay(2000);
  digitalWrite(GELB,LOW);
  delay(2000);
  digitalWrite(ROTA,HIGH);
  delay(4000);
  digitalWrite(ROT,LOW);
  delay(2000);
  digitalWrite(GRUEN,HIGH);
  delay(5000);
  digitalWrite(GRUEN,LOW);
  delay(2000);
  digitalWrite(ROT,HIGH);
  delay(4000);
  digitalWrite(GELB,HIGH);
  delay(2000);
  digitalWrite(ROTA,LOW);
  delay(2000);
  digitalWrite(GELB,LOW);
  delay(500);
  digitalWrite(GRUENA, HIGH);
  }


}// Ende der Schleife
