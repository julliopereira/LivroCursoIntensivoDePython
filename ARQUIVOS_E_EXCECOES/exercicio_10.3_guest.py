# ESCREVER UM PROGRAMA QUE PEÇA O NOME DO USUARIO E GRAVE NO ARQUIVO CHAMADO guest.txt

nome = input('Digite seu nome: ')
arq = input('Digite o nome do arquivo: ')
path = ('/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES/' + arq)

with open(path, 'a') as f_obj:
    f_obj.write(nome)

with open(path) as file_obj:
    arquivo = file_obj.read()
    print('\n\nSeu nome é: \n' + arquivo.)


