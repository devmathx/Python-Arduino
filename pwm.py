# Utilizando o PWM

from numpy import arange
from pyfirmata import Arduino
from time import sleep 

placa = Arduino("COM3") # Configurar porta USB

pin = placa.get_pin("d:10:p")
for pwm in arange(0, 1, 0.04): # arange(start, stop, step)
    pin.write(pwm)
    sleep(0.07) # Funciona como o "delay" do Arduino, valor em segundos

placa.exit() # Finalizar comando de maneira limpa