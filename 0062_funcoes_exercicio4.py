### ALBUM

albuns = []

def func_make_album(n_artista, n_album, n_faixas):
    dic = {'artista':n_artista, 'album':n_album, 'faixas': n_faixas }
    albuns.append(dic)

print('\n---- Realizando Pesquisa ----')
while True:
    artista = input('\nDigite artista: ')
    if artista == 'q':
        break
    album = input('\nDigite Album: ')
    if album == 'q':
        break
    faixas = input('\nNumero de faixas: ')
    if faixas == 'q':
        break
    if artista or album or faixas == 'q':
        break

    dicionarios = func_make_album(artista, album, faixas)


for album in albuns:
    print('\n\t Album: ' + album)
    for k, v in album.items():
        print('\n\n\t' + k.title() + ':', v.title())

