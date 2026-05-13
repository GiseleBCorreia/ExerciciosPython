dados=list()
principal=list()

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    principal.append(dados[:])
    dados.clear()
    opcao=str(input('Deseja cadastrar mais alguém? [S/N]')).strip().upper()
    if opcao == 'N':
        break

print(f'Foram cadastradas {len(principal)}pessoas')
principal.sort(reverse=True)
print(f'As pessoas mais pesadas são:{principal[0:2][0]}')
principal.sort()
print(f'As pessoas mais leves são:{principal[0:2][0]}')

NAO CONSEGUI

