lista=list()
lista1=list()
lista2=list()
while True:
     n=int(input('Digite um valor:'))
     lista.append(n)
     if n % 2==0:
        lista1.append(n)
        print('Valor adicionado a lista de número par com sucesso!')
     else:
        lista2.append(n)
        print('Valor adicionado a lista de número ímpar com sucesso!')

     opcao=str(input('Você quer continuar? [S/N]')).strip().upper()
     if opcao=='N':
        break
print(f'A lista geral é {lista}')
print(f'A lista de números pares é {lista1}')
print(f'A lista de números ímpares é {lista2}')


