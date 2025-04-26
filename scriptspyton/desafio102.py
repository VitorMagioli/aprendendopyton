def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return(print(f'{f} '))

                
help(fatorial)
fatorial(5, True)
