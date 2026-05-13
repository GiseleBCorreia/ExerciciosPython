resultado=dict()
resultado['Nome']=str(input('Nome:')).strip().upper()
resultado['Média']=float(input(f'Média de {resultado['Nome']}: '))
if resultado['Média']>= 6.0:
    resultado['Situação']='Aprovado'
    print(f'Parabéns! Você foi {resultado['Situação']}')
else:
    resultado['Situação'] = 'Reprovado'
    print(f'Que pena! Você foi {resultado['Situação']}')

