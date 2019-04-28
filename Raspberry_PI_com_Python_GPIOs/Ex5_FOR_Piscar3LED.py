#Ligar 1 LED

#Importa biblioteca para controle das GPIO
import RPi.GPIO as gpio

#Importa biblioteca para controle de tempo
import time

#GPIO.BOARD = numeros impressoras na placa
#GPIO.BCM   = numeros pelos pinos de saída GPIO

gpio.setmode(gpio.BCM)


#Define o pino 31 da placa como saida
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

for repete in range(0,10):
    gpio.output(16, gpio.HIGH)
    gpio.output(20, gpio.HIGH)
    gpio.output(21, gpio.HIGH)
    time.sleep(0.1)
    gpio.output(16, gpio.LOW)
    gpio.output(20, gpio.LOW)
    gpio.output(21, gpio.LOW)
    time.sleep(0.1)
    print(repete);#Mostra o valor da variavel repete

gpio.cleanup()


