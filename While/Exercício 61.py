contador = 0
soma = 0

while True:

    numero = int(input("Digite um número (Valor negativo interrompe o programa): "))

    if numero<0:
        break

    print(f'A tabuada do {numero} é:')

    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    
    
print('Fim do programa')
    
