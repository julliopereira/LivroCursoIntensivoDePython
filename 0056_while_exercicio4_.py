### LANCHONETE  - CRIAR LISTA DE SANDWICHS E PREENCHER COM NOMES DE SANDWICHES
### MOSTRAR O NOME A MEDIDA QUE FOREM PREPARADOS


sandwich_orders = ['tomate', 'pichles', 'queijo prato', 'alface', 'picanha', 'ovo']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('O sandwich de ' + sandwich.title() + ' foi preparado.')
    finished_sandwiches.append(sandwich)

print('\nSandwitchs finalizados: ')
for sandwich in finished_sandwiches:
    print('\tSandwitch pronto: ' + sandwich.title())


