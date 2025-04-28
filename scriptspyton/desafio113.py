def leiaInt(msg, valor = 0):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg))
            n.isnumeric()
            valor = int(n)
            ok = True
        except KeyboardInterrupt:
            print('\33[0;31mO usuário preferiu não digitar esse número. \33[m')
            break
        except:
            print('\33[0;31m[ERRO] Digite um número inteiro válido! \33[m')
        if ok:
            break
    return valor


def leiaFloat(msg, valor = 0):
    ok = False
    valor = 0
    while True:
        try:
            n = str(input(msg))
            n.isnumeric()
            valor = float(n)
            ok = True
        except KeyboardInterrupt:
            print('\33[0;31mO usuário preferiu não digitar esse número. \33[m')
            break
        except:
            print('\33[0;31m[ERRO] Digite um número REAL válido! \33[m')
        if ok:
            break
    return valor
               

#Programa Principal

inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'Você digitou o número inteiro {inteiro} e o número real {real}.')
