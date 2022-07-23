from pyfirmata import Arduino

placa = Arduino("COM3")

pin = int(input('Selecione a porta: [9,10] '))
porta = placa.get_pin(f"d:{pin}:p")

while True:
    value = str(input('Controle o LED: ')) 
    if value == 'sair': break
    elif value == 'pin': 
        pin = int(input('Selecione a porta: [9,10] '))
        porta = placa.get_pin(f"d:{pin}:p")
    else: porta.write(float(value) / 100)
    
placa.exit()
