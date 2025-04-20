print('-=-'*10)
print('        BANCO MAGIOLI')
print('-=-'*10)

print('Bem-vindo!')
print('Cédulas disponíveis: R$50, R$20, R$10, R$5, R$1')
saque = int(input('Qual valor você quer sacar? R$ '))
total = saque
ced = 50
totced = 0

while True:
    if total >= ced:
        total -= ced
        totced +=1

    else:
        if totced > 0:
            print(f'Você sacou {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        
        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 5
        
        elif ced == 5:
            ced = 1

        totced = 0 #toda vez que muda a nota zera a contagem de cédulas.
        
        if total == 0:
            break

print('==='*10)
print('Volte sempre ao Banco MAGIOLI!')