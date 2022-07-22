### CRIAR UMA LISTA admin COM 5 USUARIOS

usuarios = ['maria', 'paulo', 'silvia', 'joao', 'ciro', 'jose', 'admin']

### ESCREVER UMA SAUDAÇÃO PARA CADA USUÁRIO APÓS LOGIN
login = 'joao'

for usuario in usuarios:
    if login.lower() in usuario:
        print('\nOlá senhor "' + str(usuario).title() + '" você está entrando no sistema... \n' )

### 
print('-'*50)