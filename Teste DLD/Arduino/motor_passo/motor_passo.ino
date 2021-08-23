#include <AccelStepper.h>
int velocidade_motor = 400;
int aceleracao_motor = 200;

int input = 0;
// Definicao pino ENABLE
int pino_enable = 10;
// Definicao pinos STEP e DIR
AccelStepper motor1(1,7,4 );

void setup() {
  Serial.begin(9600);
  pinMode(pino_enable, OUTPUT);
  // Configuracoes iniciais motor de passo
  motor1.setMaxSpeed(velocidade_motor);
  motor1.setSpeed(velocidade_motor);
  motor1.setAcceleration(aceleracao_motor);
  print_msg();

}

void print_msg() {
  Serial.println("Digite:");
  Serial.println("0 - Portrait");
  Serial.println("1 - Landscape Left");
  Serial.println("2 - Landscape Right");
  Serial.println("3 - Upside Down");
}

void loop() {
  if (Serial.available() > 0)
  {
    input = Serial.read();
    if (input == '0')
    {
      motor1.moveTo(100);
    }
    if (input == '1')
    {
      motor1.moveTo(150);
    }

    if (input == '2')
    {
      motor1.moveTo(200);
    }

    if (input == '3')
    {
      motor1.moveTo(50);
    }
    if (input == '4')
    {
      digitalWrite(pino_enable, HIGH);
    }
    if (input == '5')
    {
      digitalWrite(pino_enable, LOW);
    }
    if (input == '6')
    {
      motor1.moveTo(5000);
    }

  }

  

  motor1.run();

}
