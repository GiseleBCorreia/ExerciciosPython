matriz=[[],[],[]]
pares=list()
impar=list()
coluna3=list()

for l in range(3):
    for c in range(3):
        valor=int(input(f'Digite um valor para posição [{l}, {c}]:'))
        matriz[l].append(valor)
        if valor % 2 == 0:
            pares.append(valor)
        if c==2:
            coluna3.append(valor)

print('-=' * 20)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 20)
print(f'A soma dos valores pares é igual a {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')



