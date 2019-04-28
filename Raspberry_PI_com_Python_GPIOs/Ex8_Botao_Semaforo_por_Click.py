#Ligar 1 LED
contador = 0
#Importa biblioteca para controle das GPIO
import RPi.GPIO as gpio

#Importa biblioteca para controle de tempo
import time

#GPIO.BOARD = numeros impressoras na placa
#GPIO.BCM   = numeros pelos pinos de saída GPIO

gpio.setmode(gpio.BCM)


#Define os pinos da placa como saida
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)

#Define o pino do botao como entrada
gpio.setup(12, gpio.IN)

#Apaga os leds
gpio.output(16, gpio.LOW)
gpio.output(20, gpio.LOW)
gpio.output(21, gpio.LOW)


while True:
    print(contador)
    if gpio.input(12) == gpio.HIGH:
        contador = contador + 1
        time.sleep(0.5)
        print(contador)
        
    if contador == 1:
       gpio.output(16, gpio.HIGH)
       gpio.output(20, gpio.LOW)
       gpio.output(21, gpio.LOW)
           
    if contador == 2:
       gpio.output(16, gpio.LOW)
       gpio.output(20, gpio.HIGH)
       gpio.output(21, gpio.LOW)

    if contador == 3:
       gpio.output(16, gpio.LOW)
       gpio.output(20, gpio.LOW)
       gpio.output(21, gpio.HIGH)
    

    if contador == 4:
       gpio.output(16, gpio.LOW)
       gpio.output(20, gpio.LOW)
       gpio.output(21, gpio.LOW)
       contador = 0

gpio.cleanup()


