### return DEVOLTE PARA QUEM CHAMA O VALOR FINAL DE UMA FUNÇÃO

def func_nome_formatado(first_name, last_name):
    """Devolve um nome compleso usando return"""
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

musico = func_nome_formatado('jimi', 'hendrix')
print(musico)