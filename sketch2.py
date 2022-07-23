from pyfirmata import Arduino

placa = Arduino("COM3")

def alterarNome():
    oldName = str(input("Qual porta mudar: "))
    newName = str(input('Digite o novo nome: '))
    portas[newName] = portas.pop(oldName)

portas = {
    'R': placa.get_pin('d:8:o'),
    'G': placa.get_pin('d:9:o'),
    'B': placa.get_pin('d:10:o'),
}
while True:
    nome = str(input("Escolha uma porta: "))
    if nome == 'sair': break
    elif nome == 'mudar': alterarNome()
    else: 
        valor = int(input('Escolha o valor: '))
        portas[nome].write(valor)
    
placa.exit()