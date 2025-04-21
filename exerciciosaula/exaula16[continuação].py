a = (2, 3, 5)
b = (1, 2, 4, 5, 8)

#mostrando na tela as tuplas
print(a)
print('\n')
print(b)
print('\n')

#concatenando as tuplas e mostrando na tela
c = a + b
print(c)
print('\n')

d = b + a
print(d)
print('\n')

#tamanho da tupla
print(len(a))
print('\n')
print(len(c))
print('\n')

#count (QUANTAS VEZES está aparecendo o número 5 (elemento) dentro da tupla "C")
print(c.count(5))

#quantas vezes está aparecendo o elemento "4" na tupla "D"
print(d.count(4))

#index (EM QUE POSIÇÃO está o elemento "8")
print(c.index(8))

#index com deslocamento(número depois da vírgula para começar a contar a partir da posição 2, desconsiderando 0 e 1)
print(d.index(2, 2))

#tipos de dados diferentes dentro das tuplas
pessoa = ('Vitor', 28, 'M', 1.79, 76)
print(pessoa)