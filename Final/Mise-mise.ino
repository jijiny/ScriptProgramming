int Vo = A1;
int V_LED = 3;
int count = 0;

float Vo_value = 0;
float Voltage = 0;
float dust = 0;

void setup() {
  Serial.begin(9600);
  pinMode(V_LED, OUTPUT);
  pinMode(Vo, INPUT);
}

void loop() {
  digitalWrite(V_LED, LOW);
  delayMicroseconds(280);
  Vo_value = analogRead(Vo);
  delayMicroseconds(40);
  digitalWrite(V_LED, HIGH);
  delayMicroseconds(9680);

  Voltage = Vo_value * 5.0 / 1024.0;
  dust = (Voltage - 0.6) / 0.005;
  
  Serial.println(dust);
  delay(1000);
  }

  
  

