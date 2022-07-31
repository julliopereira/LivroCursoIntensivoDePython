### ALTERAR USUARIOS NÃO CONFIRMADOS PARA CONFIRMADOS 

unconfirmed_users = {'alice', 'brian', 'candace'}           # CRIADO DICIONARIO COM OS NOMES
confirmed_users = []                                        # CRIADO LISTA

while unconfirmed_users:                                    # ENQUANTO EXISTIR UM USUARIO NO DICIONARIO
    current_user = unconfirmed_users.pop()                  # RETIRA O ULTIMO USUARIO DO DICIONARIO E GRAVA O NOME NA VARIAVEL current_user
    print('Verificando usuario: ' + current_user + '!.')
    confirmed_users.append(current_user)                    # ADICIONA O USUARIO NA LISTA confirmed_users

for confirmed_user in confirmed_users:
    print('O usuário ' + confirmed_user + )
