### ALBUM




def func_make_album(n_artista, n_album, n_faixas):
    n_artista = {'artista':n_artista, 'album':n_album, 'faixas': n_faixas }
    return n_artista

def func_add_dados(n_artista, n_album, n_faixas)

artista = input('Digite artista: ')
album = input('Digite Album: ')
faixas = input('Numero de faixas: ')

albuns = func_make_album(artista, album, faixas)


for k, v in albuns.items():
    print('\n' + k + ':' + v)

