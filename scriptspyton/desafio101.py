def voto(n):
    from datetime import datetime
    anoatual = datetime.now().year
    id = anoatual - n
    if(id >= 18 and id < 65):
        return(print(f'Você tem {id} anos. VOTO OBRIGATÓRIO.'))
    elif(id >= 16 or id >= 65):
        return(print(f'Você tem {id} anos. VOTO OPCIONAL.'))
    else:
        return(print(f'Você tem {id} anos. VOTO NEGADO.'))

#Programa Principal
nasc = int(input('Ano de Nascimento: '))
voto(nasc)
