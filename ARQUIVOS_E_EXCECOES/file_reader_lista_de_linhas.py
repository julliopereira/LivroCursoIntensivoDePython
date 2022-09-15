 LER O ARQUIVO pi_digits.txt

print(f'MOSTRA CONTEUDO DO ARQUIVO MAS COM ESPACOS:')
file_path = '/home/julio/Documentos/git/LivroCursoIntensivoDePython/ARQUIVOS_E_EXCECOES'
with open(file_path + '/pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    for line in file_object:
        print(line)                                          # MOSTRAR CONTEÚDO DE line