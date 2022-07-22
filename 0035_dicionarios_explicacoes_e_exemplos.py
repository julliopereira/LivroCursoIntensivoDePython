### DICIONARIOS

'''
Dicionários são representados por colchetes { } e 
funciona um pouco parecido como Listas no entanto 
cada valor tem duas instruções chamados chave e 
valor.
{ chave: valor, chave: valor } 
'''

### EXEMPLO 1 - SOLICITANDO O VALOR DA CHAVE 'cor':
print('-'*50)

alien_0 = {'cor': 'verde', 'pontos': 5}     # DICIONARIO COM 2 PARES { 'chave:valor', 'chave:valor'} 

print(alien_0['cor'] + '\n')                # SOLICITANDO VALOR DE UM DICIONÁRIO COM PRINT

### EXEMPLO 2 - SOLICITANDO O VALOR DA CHAVE 'pontos' SE UTILIZANDO DE VARIAVEL:
print('-'*50)

alien = alien_0['pontos']

print(alien)


