# Versão 0.02
from pyfirmata import Arduino

placa = Arduino("COM3")

while True:
    porta = int(input('Selecione a porta: [8,9,10] '))
    quest = str(input('Controle o LED: '))
    if quest == 'ligar': placa.digital[porta].write(1)
    elif quest == 'desligar': placa.digital[porta].write(0)
    elif quest == 'sair': break
    else: print('Comando não reconhecido') 
        
placa.exit()
