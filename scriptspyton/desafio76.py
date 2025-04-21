listagem_Produtos = ('Pão (kg)', 10.65, 
                     'Leite', 4.50, 
                     'Queijo 100g', 5.99, 
                     'Açúcar 1kg', 3.99)

print('='*20)
print('LISTAGEM DE PRODUTOS')
print('='*20)
for pos in range(0, len(listagem_Produtos)):
    if pos % 2 == 0:
        print(f'{listagem_Produtos[pos]:.<30}', end='')
    else:
        print(f'{listagem_Produtos[pos]:<30.2f}')