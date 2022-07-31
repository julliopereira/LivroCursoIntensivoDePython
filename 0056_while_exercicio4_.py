### LANCHONETE  - CRIAR LISTA DE SANDWICHS E PREENCHER COM NOMES DE SANDWICHES
### MOSTRAR O NOME A MEDIDA QUE FOREM PREPARADOS


sandwich_orders = ['tomate', 'pastrami', 'pichles', 'pastrami', 'queijo prato', 'alface', 'picanha', 'ovo', 'pastrami']
finished_sandwiches = []

print('Preparando os lanches: ')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\tO sandwich de ' + sandwich.title() + ' foi preparado.')
    finished_sandwiches.append(sandwich)

print('\nSandwitchs finalizados: ')
for sandwich in finished_sandwiches:
    print('\tSandwitch pronto: ' + sandwich.title())


print('-'*50) #-----------------------------------------------------------------------------------
### INFORMAR AOS CLIENTES QUE A LANCHONETE ESTA SEM pastrami E REMOVER DA LISTA

sandwich_orders = ['tomate', 'pastrami', 'pichles', 'pastrami', 'queijo prato', 'alface', 'picanha', 'ovo', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print('\nPreparando os lanches: ')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('\tO sandwich de ' + sandwich.title() + ' foi preparado.')
    finished_sandwiches.append(sandwich)

print('\nSandwitchs finalizados: ')
for sandwich in finished_sandwiches:
    print('\tSandwitch pronto: ' + sandwich.title())

