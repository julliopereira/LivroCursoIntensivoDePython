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

for k, v in usuarios.items():
    print(str(k) + ':' + str(v))
print('\n')

### 
print('-'*50)