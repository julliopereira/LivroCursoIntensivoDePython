### USAR WHILE PARA GERAR UM LOOP INFINITO DE SAUDAÇÃO COM DEVULUÇÃO return

def func_saudacao(nome, sobrenome):
    var_full_name = nome.title() + ' ' + sobrenome.title()
    return var_full_name

while True:
    print('\nPor favor digite seu nome e sobrenome: ')
    var_nome = input('\n\tDigite seu nome: ')
    var_sobrenome = input('\n\tDigite seu sobrenome: ') 
