### CRIAR UMA LISTA admin COM 5 USUARIOS

admin = ['maria', 'paulo', 'silvia', 'joao', 'ciro', 'jose']

### ESCREVER UMA SAUDAÇÃO PARA CADA USUÁRIO APÓS LOGIN
login = 'joao'

for a in admin:
    if login.lower() in a:
        print('\nOlá senhor "' + str(a).title() + '" você está entrando no sistema... \n' )

### 
print('-'*50)