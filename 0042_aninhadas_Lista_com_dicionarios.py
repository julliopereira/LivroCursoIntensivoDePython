### EXPLICAÇÃO.

'''
Muitas vezes você quer adicionar um dicionarío como valor de uma lista, 
ou seja, em uma posição de uma lista você pode ter várias informações 
contidas em um dicionário.

'''

# DICIONARIOS:

pessoa_1 = {'nome': 'rodrigo', 'idade': '20', 'altura': '1.70', 'peso': '70'}
pessoa_2 = {'nome': 'maria', 'idade': '24', 'altura': '1.66', 'peso': '65'}
pessoa_3 = {'nome': 'sara', 'idade': '23', 'altura': '1.68', 'peso': '71'}

# ADICIONANDO Ã LISTA:

lista = (pessoa_1, pessoa_2, pessoa_3)
for pessoa in lista:
    print(pessoa)

print('-'*50) #---------------------------------------------------------------------------------------

# AQUI VAMOS AGORA MONTAR ALGO PARECIDO PORÉM COM 30 PESSOAS

pessoas = []                                         # LISTA VAZIA

for pessoa in range(30):                             # O range() gera 30 ocorrencias 
    nova_pessoa = {                                  # Então é criado um dissionário com 3 x chaves-valores
        'cor': 'japones', 
        'pontos': 5, 
        'velocidade': 'slow',
        }
    pessoas.append(nova_pessoa)                      # Então adicionamos à lista pessoas exatamente o dissionário criado 

for pessoa in pessoas[:5]:
    print(pessoa)



