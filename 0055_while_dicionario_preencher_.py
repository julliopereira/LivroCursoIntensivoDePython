### SOLICITA NOME DO PARTICIPANTE E UMA RESPOSTA ; USAR FLAG 

from timeit import repeat


responses = {}

polling_active = True

while polling_active:                                                   # ENQUANTO VERDADEIRO
    nome = input('\nQual é o seu nome? : ')
    response = input('você gostaria de escalar qual montanha? : ')
    responses[nome] = response                                          # ADICIONA A RESPOSTA (value) NA CHAVE (key) NOME
    repeat = input('\nVocê quer que outra pessoa responda? [si/no]')

