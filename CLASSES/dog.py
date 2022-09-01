class Dog():
    """Uma tentativa de modelar um cachorro"""
    def __init__(self,name, age):
        """Inicializa os atributos name e age."""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentando"""
        print(f'{self.name.title()} sentar!')

    def roll_over(self):
        """Simula um cachorro rolando"""
        print(f'{self.name.title()} rolar!')

cachorro = Dog('wille', 14)
print(f'Meu cachorro é o {cachorro.name.title()} e tem a idade de {cachorro.age} anos.')