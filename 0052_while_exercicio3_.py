### USAR TODOS OS TERMOS APRENDIDOS

ingr = ''

print('Digite os ingredientes para a pizza: \n')


while ingr != 'quit':
    ingr = input('\tIngrediente: ')
    if ingr == 'quit':
        break

while True:
    pagar = input('Como deseja pagar ?')
    if pagar != '':
        continue
    else:
        break

print('Ótimo pedido, estamos preparando sua pizza...')