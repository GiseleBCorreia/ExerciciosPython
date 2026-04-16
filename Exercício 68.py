import random
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
vitorias=0
While true:
    c=random.randint(1,10)
    n1=int(input('Digite um valor:')
    a2=str(input('Par ou ímpar [P/I]')).strip().upper()
    total=n1+c
    if total%2=0:
        resultado='P'
    else:
        resultado='I'
    print('------------------------------')
    print(f'Você jogou {n1} e o computador jogou {c} total deu {total}')
    if a2==resultado:
      print('Você Venceu!')
    else:
        print('Você perdeu!')
        break
print(f'Game over! Você venceu {vitorias} vezes.')
