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

### 
print('-'*50)

