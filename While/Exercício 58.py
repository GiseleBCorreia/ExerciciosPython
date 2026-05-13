import random
numero= random.randint(0, 10)
n1=int(input('Tente adivinhar o número que eu pensei entre 0 e 10: '))
while n1 != numero:
    print('Número errado! Tente novamente.')
    n1=int(input('Tente adivinhar o número que eu pensei entre 0 e 10: '))
print(f'Parabéns! Você acertou! O número que eu pensei foi {numero}.')