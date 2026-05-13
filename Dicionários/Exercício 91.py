import random
from operator import itemgetter

resultado = dict()

for c in range(4):
    dado = int(input(f'Jogador número {c+1} - Digite 1 para jogar o dado: '))

    if dado == 1:
        num = random.randint(1, 6)
        print(f'O número que caiu foi {num}')
        resultado[f'Jogador {c+1}'] = num

ranking = sorted(resultado.items(), key=itemgetter(1), reverse=True)

print('\n=== RANKING ===')
for pos, jogador in enumerate(ranking):
    print(f'{pos+1}º lugar: {jogador[0]} com {jogador[1]}')