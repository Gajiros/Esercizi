class Restaurant_import:

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant_import(self):

        print(f'restaurant name: {self.restaurant_name}, cousine type: {self.cuisine_type}.')

    def open_restaurant_import(self):

        print('the restaurant is open.')

    def set_number_served_import(self, number_served: int):

        self.number_served = number_served

    def increment_number_served_import(self, number_served: int):

        self.number_served += number_served