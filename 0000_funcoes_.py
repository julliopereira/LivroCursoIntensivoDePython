### FUNÇÕES

## VARIADO

dez = range(2, 10)                          # range     - GRAVE NA VARIAVEL 'dez' OS VALORES DE 2 A 10
print(dez)

## LISTA 

lista = ['honda', 'hyundai', 'gm', 'volks']

print(lista)
print(sorted(lista))                        # sorted    - Em ordem alfabética
print(sorted(lista, reverse=True))          # sorted    - Em ordem alfabética porém inversa sem alterar valores
print(len(lista))                           # len       - Mostra o tamanho da lista (se tiver cinco valores a saída é o número 5) nosso caso 4
print(list(range(1, 6+1)))                  # list      - Com a ajuda de range() pode gerar uma lista com números sequenciais

digitos = list(range(10))
print(min(digitos))                         # min       - Mostra o menor numero da lista
print(max(digitos))                         # max       - Mostra o maior numero da lista
print(sum(digitos))                         # sum       - A soma de todos os dígitos


