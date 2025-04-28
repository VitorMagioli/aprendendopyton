try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    res = a / b

#except Exception as erro:
#    print(f'Problema encontrado: {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado informado. Por favor, digite apenas números.')
except ZeroDivisionError:
    print('Não é possível realizar a divisão por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
except Exception as erro:
    print(f'A causa do erro foi {erro.__cause__} da classe {erro.__class__}')
else:
    print(f'O resultado é {res:.1f}')

finally:
    print('Obrigado! Volte sempre.')
