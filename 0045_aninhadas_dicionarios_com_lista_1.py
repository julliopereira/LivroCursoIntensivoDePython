### USANDO DICIONÁRIOS DENTRO DE LISTAS

linguagens_favoritas = {
    'joao': ['python', 'c'],
    'sara': ['c'],
    'eduardo': ['ruby', 'java'],
    'jorge': ['python'],
    }

for nome, linguagem in linguagens_favoritas.items():
    if len(linguagem) > 1:
        print(nome,'As linguagens que você escolheu são: ')
        for ling in linguagem: 
            print('\t',ling)
            
    elif len(linguagem) == 1:
        print(nome,'a linguaguem que você escolheu é: ',linguagem)
    