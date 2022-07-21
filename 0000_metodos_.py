
from turtle import clear

### VARIADO




### TEXTO
text = 'maria jose arado'

print(text.title())                     # title - Torna primeiras Letras do text maiúsculas
print(text.upper())                     # upper - Altera todos os caracteres da variável para MAIUSCULAS
print(text.lower())                     # lower - Altera todos os caracteres da variável para minusculas
print(text.rstrip())                    # rstip - Remover ESPAÇOS a direita
print(text.lstrip())                    # rstip - Remover ESPAÇOS a esquerda
print(text.lstrip())                    # rstip - Remover ESPAÇOS a direita e esquerda


### LISTAS
lista = ['honda', 'ducatti', 'yamaha']

lista.append('bmw')                            # append - Adiciona valor na ultima posição da lista
lista.insert(0, 'bmw')                         # insert - Adiciona valor 'bmw' na posição 0
var = lista.pop()                              # pop    - Remove último valor da lista e grava valor na variavel 'var'   
var = lista.pop(1)                             # pop    - Remove valor na posição 1 e grava valor na variavel 'var'
lista.remove('bmw')                            # remove - Remove o valor 'bmw' da lista não importando em que posição esteja
del lista[0]                                   # del    - Remove valor na posição 0
del lista                                      # del    - Remove lista
lista = ['honda', 'ducatti', 'yamaha']
lista.sort()                                   # sort   - Altera a lista em ordem alfabetica [PERMANENTE]
lista.sort(reverse=True)                       # sort   - Ordena porém em ordem reversa      [PERMANENTE]
lista.reverse()                                # reverse- Alterar o SENTIDO da lista ( o ultimo vira primeiro e o primeiro vira último)




