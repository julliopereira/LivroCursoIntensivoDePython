### USANDO DICIONÁRIOS DENTRO DE LISTAS

linguagens_favoritas = {
    'joao': ['python', 'c'],
    'sara': ['c'],
    'eduardo': ['ruby', 'java'],
    'jorge': ['python'],
    }

for nome, linguagem in linguagens_favoritas.items():
    print(nome,':',linguagem)