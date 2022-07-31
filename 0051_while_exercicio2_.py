### DIFERENTES VALORES DE PREÇO DE INGRESSO DE ACORDO COM IDADE
### 3 anos = gratuito | 3-12 = 10 dolares | 13 - = 15 dolares

print('Digite sua idade para obter seu ingresso: \n')

while True:
    idade = int(input('\t Digite a idade: '))
    if idade <= 3:
        print('O ingresso é gratuito')
        break
    elif idade <= 12:
        print('O valor do ingresso é 10 dolares')
        break
    else:
        print('O valor do ingresso é 15 dolares')
        break
