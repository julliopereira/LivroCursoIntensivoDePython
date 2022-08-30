# CRIAR UMA LISTA DE NOMES DE MAGICOS E PASSA A LISTA PARA UMA FUNCAO QUE EXIBA O NOME DOS MAGICOS

magicos = ['miranda', 'mauro', 'xman', 'tendu', 'magic']    # CRIANDO LISTA

def show_magicians(magicos):                                # CRIANDO FUNCAO 
    for magico in magicos:
        print(magico)                                       # MOSTRANDO MAGICO

def make_great(magicos):
    c = 0
    for magico in magicos:
        nome = print(f'{magico} O Grande!')
        magicos.insert(c, nome)
        c =+ 1

make_great(magicos)

show_magicians(magicos)                                     # CHAMANDO FUNCAO