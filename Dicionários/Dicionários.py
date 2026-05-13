'''
pessoas={'nome':'Gustavo', 'Sexo':'M', 'idade':22}
del pessoas['Sexo']
pessoas['nome']='Gisele'
pessoas['peso']=98.5
print(pessoas)
print(pessoas['idade'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v} ')
'''
'''
brasil=[]
estado1={'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2={'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1])
print(brasil[1]['sigla'])
'''
estado=dict()
brasil=list()
for c in range(3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    #forma de uma lista copiar um dicionário:
    brasil.append(estado.copy())
for e in brasil:
    print(e)
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k}, tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v)

print(brasil)



