### FAÇA VOCE MESMO

# CRIAR DOIS NOVOS DICIONARIOS QUE  REPRESENTEM PESSOAS DIFERENTE E ARMAZENE EM UM DICIONARIO
# ARMAZENE OS TRES DICIONARIOS EM UMA LISTA CHAMADA people. PERCORRA SUA LISTA DE PESSOAS COM UM LAÇO.
# A MEDIDA QUE PERCORRER A LISTA APRESENTE TUDO QUE VOCÊ SABE SOBRE CADA PESSOA

pessoas = { 
    'mario' : { 
        'nome': 'mario',
        'sobrenome': 'ayala',
        'altura': '1.80',
        'peso': '80',
        'civil': 'solteiro',
        'esporte': 'futebol',
        'trabalho': 'engenheiro',
        },

    'maria' : { 
        'nome': 'maria',
        'sobrenome': 'mendes',
        'altura': '1.65',
        'peso': '60',
        'civil': 'solteira',
        'esporte': 'voley',
        'trabalho': 'tecnica',
        },

    'julio' : { 
        'nome': 'julio',
        'sobrenome': 'pereira',
        'altura': '1.84',
        'peso': '90',
        'civil': 'solteiro',
        'esporte': 'futebol',
        'trabalho': 'Adm de rede',
        },
    }

for nome, nome_info in pessoas.items():
    print('\nO seu nome de usuário é :' + nome)
    print('\n')