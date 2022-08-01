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
    print('\n\tEu tenho um ' + tipo.title())
    print('\tE o nome dele é ' + nome.title() + '\n')

func_animal_tipo('hamster', 'bidú')

print('-'*50) #-----------------------------------------------------------------------------
### [04] VÁRIAS CHAMADAS DA MESMA FUNÇÃO:

func_animal_tipo('dog', 'lessi')                    # NESTE EXEMPLO A ORDEM IMPORTA
func_animal_tipo('cat', 'white')
func_animal_tipo('boi', 'malhado')
func_animal_tipo('cavalo', 'fogo')

print('-'*50) #-----------------------------------------------------------------------------
### [05] ALTERANDO A ORDEM  :

func_animal_tipo('boi', 'malhado')
func_animal_tipo(nome='fogo', tipo='cavalo')                # AQUI ALTERADA ORDEM NO ENTANDO FOI ESPECIFICADO O ARGUMENTO  

print('-'*50) #-----------------------------------------------------------------------------
### [05] VALORES DEFAULT  :

def func_animal_tipo2(tipo='dog', nome):                    # SE NENHUM ARGUMENTO PARA tipo FOR ENTÃO É MOSTRADA OP
    """Exibe informações sobre animal """
    print('\n\tEu tenho um ' + tipo.title())
    print('\tE o nome dele é ' + nome.title() + '\n')

func_animal_tipo2('hamster', 'bidú')

print('-'*50) #-----------------------------------------------------------------------------
### [07] MAIS ARGUMENTOS QUE O ESPERADO PELA FUNÇÃO:

func_animal_tipo('dog', 'lessi', '10kG')                    # VAI DAR ERRO, A FUNÇÃO ESPERA APENAS 2
