r=''
while r != 'M' and r != 'F':
    r = str(input('Digite seu sexo [M/F]: ')).strip().upper()
print(f'Sexo {r} registrado com sucesso!')
