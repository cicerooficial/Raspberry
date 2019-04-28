#Ascender 3 LED

#Importa biblioteca para controle das GPIO
import RPi.GPIO as gpio

#GPIO.BOARD = numeros impressoras na placa
#GPIO.BCM   = numeros pelos pinos de saída GPIO

gpio.setmode(gpio.BCM)


#Define o pino 31 da placa como saida
gpio.setup(16, gpio.OUT)
gpio.setup(20, gpio.OUT)
gpio.setup(21, gpio.OUT)



gpio.output(16, gpio.HIGH)
gpio.output(20, gpio.HIGH)
gpio.output(21, gpio.HIGH)


#gpio.cleanup()
