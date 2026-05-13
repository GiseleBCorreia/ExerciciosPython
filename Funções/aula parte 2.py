'''def contador(i,f,p):
    c=i
    while c <= f:
        print(f'{c} ', end='')
        c+=p
    print('FIM')

contador(2,10, 2)'''

def soma(a=0, b=0, c=0):
    s=a+b+c
    return s
r1=somar(3, 2, 5)
r2=somar(2, 2)
r3=somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')