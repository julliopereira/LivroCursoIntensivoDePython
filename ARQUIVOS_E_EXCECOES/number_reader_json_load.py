# json.load() - LÊ A LISTA DE VOLTA DO ARQUIVO PARA MEMÓRIA:

import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)      # ADICIONA O CONTEÚDO DO ARQUIVO numbers.json NA VARIÁVEL numbers

print(numbers)                      # MOSTRA O CONTEÚDO DA VARIÁVEL