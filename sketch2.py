from pyfirmata import Arduino

placa = Arduino("COM3")

def alterarNome():
    oldName = str(input("Qual porta mudar? "))
    newName = str(input('Digite o novo nome: '))
    portas[newName] = portas.pop(oldName)

def ehPwm():
    porta = str(input("Qual porta? "))
    pin = (str(portas[porta]).split())[2]
    if int(pin) in [3, 5, 6, 9, 10, 11]:
        return print(f"Sim, a porta {pin} é PWM.")
    else: return print(f"Não, a porta {pin} não é PWM.")

portas = {
    'R': placa.get_pin('d:8:o'),
    'G': placa.get_pin('d:9:p'),
    'B': placa.get_pin('d:10:p'),
}

while True:
    nome = str(input("Escolha uma porta: "))
    if nome == 'sair': break
    elif nome == 'mudar': alterarNome()
    elif nome == 'pwm': ehPwm()
    else: 
        valor = float(input('Escolha o valor: '))
        portas[nome].write(valor)
   
placa.exit()