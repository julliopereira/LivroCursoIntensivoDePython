### UTILIZANDO LAÇO PARA PERCORRER A LISTA

'''
É importante entender que para puxar o valor de key ou valores
deve-se utilizar o MÉTODO items() que engloba keys() e values() no laço.
'''

print('-'*50)
usuarios = {
    'usuario': 'rodrigo',
    'nome': 'rodrigo',
    'sobrenome': 'pontes',
    }

for k, v in usuarios.items():               # ATRIBUI ÀS VARIÁVEIS k e v OS VALORES PARES DO DICICIONARIO 
    print(str(k) + ':' + str(v))            # MOSTRA O VALOR key e values
print('\n')


### PARA TRABALHAR COM O VALOR keys É NECESSÁRIO UTILIZAR O MÉTODO keys()
print('-'*50)

num_favoritos = { 
    'joao': '30',
    'sara': '10',
    'eduardo': '20',
    'phil': '40',
    }

for nome in num_favoritos.keys():                     # ATRIBUI À VARIÁL nome OS VALORES de NOME
    print('O nome é ' + str(nome).title())            # MOSTRA O VALOR key e values
print('\n')

