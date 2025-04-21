print('CADASTRO DE PRODUTOS')
listagem_Produtos = (str(input('Digite o nome do produto: ')), float(input('Preço: R$ ')), 
                     str(input('Digite o nome do produto: ')), float(input('Preço: R$ ')), 
                     str(input('Digite o nome do produto: ')), float(input('Preço: R$ ')), 
                     str(input('Digite o nome do produto: ')), float(input('Preço: R$ ')))

print('='*20)
print('LISTAGEM DE PRODUTOS')
print('='*20)
for pos in range(0, len(listagem_Produtos)):
    if pos % 2 == 0:
        print(f'{listagem_Produtos[pos]:.<30}', end='')
    else:
        print(f'{listagem_Produtos[pos]:<30.2f}')