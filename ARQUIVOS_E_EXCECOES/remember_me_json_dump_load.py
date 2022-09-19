# VAMOS USAR json.dump() e json.load() NO MESMO ARQUIVO PARA RECUPERAR O NOME DIGITADO

import json
    
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('Qual o seu username: ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print(f'\n\tNós relembraremos você "{username}".')
else:
    print(f'\n\tBem vindo de volta "{username}"!')
