class Restaurant():
    def __init__(self,restaurant_name,cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restautant(self):
        print(f'Você está no restaurante {self.restaurant_name.title()}')
        print(f'Servimos comida {self.cousine_type.title()}')

    def open_restaurant(self):
        print(f'o restaurante {self.restaurant_name.title()} está aberto!!!')

restaurant = Restaurant('bodão', 'fast food')
print(f'{restaurant.restaurant_name.title()} {restaurant.cousine_type.title()}')
restaurant.describe_restautant()
restaurant.open_restaurant()