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