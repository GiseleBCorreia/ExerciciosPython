for i in range(1, 6):
    peso=int(input(f'Digite o peso da {i}ª pessoa:').strip())

    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

print("Maior:", maior)
print("Menor:", menor)