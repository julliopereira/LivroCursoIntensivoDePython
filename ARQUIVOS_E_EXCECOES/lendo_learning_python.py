# EXERCICIO PARA LER O ARQUIVO learning_python.txt

arq = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/learning_python.txt'
with open(arq) as arquiv:
    arquivo = arquiv.read()
    print(arquivo)

    for line in arquiv:
        print(line.rstrip())

"""
with open(arq) as arqu:
    arquivo = arqu.readlines()
    for line in arquivo:
        print(line)
"""




