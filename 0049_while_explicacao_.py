### DIFERENTE DO LAÇO for O LAÇO while EXECUTA ENQUANTO O USUARIO QUISER PERMANECER NELE

contador = 1

while contador <= 5:                                        # SE O CANTADOR MENOR OU IGUAL A CINCO FAÇA O QUE ESTÁ DENTRO DE while
    print('contador: ' + str(contador) + ' menor que 6')
    contador += 1


print("-"*50) #---------------------------------------------------------------------
#### USURIO VAI DIGITAR VÁRIAS PALAVRAS A SEREM MOSTRADAS NA TELA, MAS SÓ VAI SAIR DO while QUANDO DIGITAR quit

dig = 'Digite qualquer coisa para eu mostrar'
dig += '\tDigite "quit" para encerrar'

mensagem = ''

while mensagem != 'quit':
    mensagem = input('Digite mensagem: ')
    print(mensagem)

print("-"*50) #---------------------------------------------------------------------
#### PARA NÁO MOSTRAR O QUIT NO FINAL USAR UM if SIMPLES

mensagem = ''
while mensagem != 'quit':
    mensagem = input('Digite mensagem: ')
    if mensagem != 'quit':
        print(mensagem)

print("-"*50) #---------------------------------------------------------------------
#### USANDO UMA flag QUE É UMA VARIAVEL QUE DEVE SER ALTERADA SE QUISER SAIR DO while

contador = 1

while contador <= 5:                                        # SE O CANTADOR MENOR OU IGUAL A CINCO FAÇA O QUE ESTÁ DENTRO DE while
    print('contador: ' + str(contador) + ' menor que 6')
    contador += 1

print("-"*50) #---------------------------------------------------------------------
#### DEIXANDO O USUARIO SAIR QUANDO QUISER

print("-"*50) #---------------------------------------------------------------------
#### DEIXANDO O USUARIO SAIR QUANDO QUISER
