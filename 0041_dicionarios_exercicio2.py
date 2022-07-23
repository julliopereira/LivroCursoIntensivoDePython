### UM LAÇO QUE PERCORRE AS CHAVES E AS EXIBE
print('-'*50)

esportes = {
    'fabio': 'futebol',
    'pedro': 'futebol',
    'silvia': 'voley',
    'eduardo': 'basquete',
    'marcio': 'handbol',
    'sara': 'voley',
    'clebio': 'golf',
    'maria': 'bike',
    'felipe': 'tiro',
    'bruno': 'tiro',
    'lucas': 'arco',
    }

for key, value in esportes.items():
    print(key + ':' +  value)


### MOSTRE  


### CRIE UM DICIONÁRIO QUE CONTRANHA O NOME DE TRÊS RIOS IMPORTANTES E O PAÍS QUE O RIO CORTA
### USE UM LAÇO COM UMA FRASE PARA CADA RIO DIZENDO QUAL PAIS PERCORRE
print('-'*50)

rios = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'jordão': 'israel',
    }

for key, value in rios.items():
    print('O rio ' + key.title() + ' corre pelo país ' + value .title()+ '.\n')