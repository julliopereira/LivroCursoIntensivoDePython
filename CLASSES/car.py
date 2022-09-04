### INCREMENTANDO VALOR DE ATRIBUTO COM MÉTODO

class Car():
    """Descrever um carro"""
    def __init__(self,fabrica,modelo,ano):
        """inicializa atributos que identificam um carro"""
        self.fabrica = fabrica
        self.modelo = modelo
        self.ano = ano
        self.odometro_lido = 0

    def nome_adaptado(self):
        """Exibe informações do meu novo carro"""
        print(f'{self.fabrica.title()} {self.modelo.title()} {self.ano}')

    def ler_odometro(self):
        """Exibe frase que mostra kilometragem do carro"""
        print(f'Este carro tem {self.odometro_lido} km.')

meu_novo_carro = Car('hynday', 'hb20', 2013)
print(f'Meu novo carro {}')

