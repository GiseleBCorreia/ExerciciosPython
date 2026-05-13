lista=list()
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
print(f'Você digitou os valores {lista}')
print(f'O maior valor dessa lista foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'O menor valor dessa lista foi {min(lista)} na posição {lista.index(min(lista))}')
