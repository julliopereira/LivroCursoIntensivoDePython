### CRIAR UMA LISTA admin COM 5 USUARIOS

usuarios = ['maria', 'paulo', 'silvia', 'admin', 'joao', 'ciro', 'jose']

### ESCREVER UMA SAUDAÇÃO PARA CADA USUÁRIO APÓS LOGIN
print('-'*50)
for usuario in usuarios:
    print('\nSenhor(a) "' + str(usuario).title() + '" loggin realizado! \n')

### SE O USUÁRIO FOR admin EXIBA MENSAGEM ESPECIAL SE NÃO MOSTRE MENSAGEM COMUM AOS DEMAIS COM else
print('-'*50)
login = 'admin'

for usuario in usuarios:
    if login.lower() in usuario:
        print('\nOlá senhor "' + str(usuario).title() + '" gostaria de ver um relatório de status? ... \n' )
    else:
        print('\nSenhor(a) "' + str(usuario).title() + '" loggin realizado! \n')


### ACON
print('-'*50)