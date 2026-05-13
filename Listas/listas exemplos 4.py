a=[2, 3, 4, 7]
#se colocar b=a cria uma ligação e tudo que fizer em b ou em a faz na outra lista também
b=a[:]
b[2]=8
print(f'Lista A:{a}')
print(f'Lista B:{b}')
