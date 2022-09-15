# LER O ARQUIVO pi_digits.txt

file_path = '~/Documentos/git/LivroCursoIntensivoDePython'
with open('pi_digits.txt') as file_object:      # ABRIR AQUIVO pi_digits.txt 
    contents = file_object.read()               # USAR O read() PARA LER O ARQ 
    print(contents)                             # MOSTRAR CONTEÚDO DE contents