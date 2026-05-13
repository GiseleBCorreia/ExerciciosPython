pares=list()
impares=list()
lista=list()
for c in range(0,7):
    n=int(input(f'Digite o {c+1}° número:'))

    if n % 2==0:
        pares.insert(0,n)

    else:
        impares.append(n)

pares.sort()
impares.sort()

print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')

