### FUNÇÃO É UM CONJUNTO DE INSTRUÇÕES QUE PODE SER CHAMADO A QUALQUER MOMENTO 
### [01] SIMPLES:

def func_saudacao():
    """Exibe saudação simples."""                           # DESCRIÇÃO DA FUNÇÃO UTILIZADA EM PYTHON
    print('\n\tOlá, tudo bem ! \n')

func_saudacao()                                             # CHAMANDO A FUNÇÃO

print('-'*50) #-----------------------------------------------------------------------------
### [02] PASSANDO ARGUMENTO PARA FUNÇÃO:

def func_saudacao2(username):                               # NECESSÁRIO ENCAMINHAR UM ARGUMENTO PARA FUNÇÃO
    """Exibe saudação com passagem de informações"""
    print('\n\tOlá, ' + username.title() + ' 2 !\n')

func_saudacao2('julio')                                     # PASSANDO O ARGUMENTO Julio PARA FUNÇÃO

print('-'*50) #-----------------------------------------------------------------------------
### [03] ARGUEMENTOS POSICIONAIS:

def func_animal_tipo(tipo, nome):
    """Exibe informações sobre animal """
    print('\n\tEu tenho um pet ' + tipo.title())
    print('\tE o nome dele é ' + nome.title() + '\n')

func_animal_tipo('hamster', 'bidú')