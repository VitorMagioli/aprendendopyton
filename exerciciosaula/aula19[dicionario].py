dados = dict()

#criando elementos e adicionando conteúdo
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])

#para adicionar outro elemento
dados['sexo']='M'
print(dados['sexo'])
#para excluir um elemento do dicionário
del dados['idade']

#criando um dicionário de várias linhas
#os elementos se chamam chaves ou keys
filme = {'filme':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
}

#VALOR - CHAVE - ITEM
print(filme.values())#VALOR: mostra o conteúdo das keys
print(filme.keys())#CHAVE: mostra o título do elemento(nome das keys)
print(filme.items())#ITEM: mostra tanto o conteúdo quanto o título das keys

#for do dicionario, "k" chaves e v "valores"
for k, v in filme.items():
    print(f'O {k} é {v}.')

#adicionando um dicionário numa lista
locadora = list()

locadora.append(filme)

#mostrando na tela 
print(locadora[0]['ano'])
