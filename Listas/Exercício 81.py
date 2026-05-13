lista=list()
while True:
    n=lista.append(int(input('Digite um número:')))
    print('Valor adicionado a lista sucesso!')
    opcao=str(input('Você quer continuar? [S/N]')).strip().upper()
    if opcao=='N':
        break
print('Você decidiu parar, então...')

print(f'Foram adicionados {len(lista)} números na lista')
lista.sort(reverse=True)
print(f'A lista em ordem descrecente é: {lista}')
if 5 in lista:
    print('O número 5 foi adicionado a lista!')
else:
    print('O número 5 não foi adicionado a lista')
