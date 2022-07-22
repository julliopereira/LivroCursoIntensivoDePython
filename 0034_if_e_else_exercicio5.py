### CRIAR UMA LISTA admin COM 5 USUARIOS

usuarios = ['maria', 'paulo', 'silvia', 'joao', 'ciro', 'jose', 'admin']

### ESCREVER UMA SAUDAÇÃO PARA CADA USUÁRIO APÓS LOGIN
print('-'*50)
for usuario in usuarios:
    print('\nSenhor(a)' )

### SE O USUÁRIO FOR admin EXIBA MENSAGEM ESPECIAL
print('-'*50)
login = 'admin'

for usuario in usuarios:
    if login.lower() in usuario:
        print('\nOlá senhor "' + str(usuario).title() + '" você está entrando no sistema... \n' )