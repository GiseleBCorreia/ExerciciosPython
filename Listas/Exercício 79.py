lista=list()
while True:
    v=int(input('Digite um valor:'))
    if v not in lista:
        lista.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor repetido, não será adicionado.')
    opcao=str(input('Quer continuar? [S/N]')).strip().upper()
    if opcao=='N':
        break
lista.sort()
print(f'Você digitou os valores: {lista}')
