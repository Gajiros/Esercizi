from lezione6_import import Restaurant_import
#9-1, 9-2, 9-4
class Restaurant:

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):

        print(f'restaurant name: {self.restaurant_name}, cousine type: {self.cuisine_type}.')

    def open_restaurant(self):

        print('the restaurant is open.')

    def set_number_served(self, number_served: int):

        self.number_served = number_served

    def increment_number_served(self, number_served: int):

        self.number_served += number_served
    
#risto1: Restaurant = Restaurant('Bisseria Grande Piramide Dejitto', 'Bissa')
#print(risto1.restaurant_name)
#print(risto1.cuisine_type)
#risto1.describe_restaurant()
#risto1.open_restaurant()

#risto2: Restaurant = Restaurant('da Giggi O\'Zozzzone', 'Indonesiana')
#risto3: Restaurant = Restaurant('da Lello er Mattarello', 'Mattarelli')
#risto2.describe_restaurant()
#risto3.describe_restaurant()

#restaurant: Restaurant = Restaurant('PizzeriaNigeria', 'Nigeriana')
#print(restaurant.number_served)
#restaurant.number_served = 1
#print(restaurant.number_served)
#restaurant.set_number_served(95)
#print(restaurant.number_served)
#restaurant.increment_number_served(4)
#print(restaurant.number_served)

#9-3, 9-5
class User:

    def __init__(self, first_name: str, last_name: str, email: str, age: int) -> None:
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.login_attempts = 0

    def describe_user(self):

        print(f'name: {self.first_name}, surname: {self.last_name}, email: {self.email}, age: {self.age}')

    def greet_user(self):

        print(f'Hello {self.last_name}, how is your day going?')

    def increment_login_attempts(self):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0

#user1: User = User('Valerio', 'Rossi', 'valros@gmail.com', 87)
#user2: User = User('Valerio', 'Bianchi', 'valbia@gmail.com', 78)
#user1.describe_user()
#user1.greet_user()
#user2.describe_user()
#user2.greet_user()

#user3: User = User('Gabriel', 'Verdi', 'gabver@gmail.com', '43')
#user3.increment_login_attempts()
#user3.increment_login_attempts()
#user3.increment_login_attempts()
#user3.increment_login_attempts()
#print(user3.login_attempts)
#user3.reset_login_attempts()
#print(user3.login_attempts)

#9-6
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name: str, cuisine_type: str, icecream_favors: list) -> None:
        
        super().__init__(restaurant_name, cuisine_type)
        self.icecream_flavors = icecream_favors

    def describe_flavors(self):
        
        print('Flavors:')
        for flavor in self.icecream_flavors:

            print(f'{flavor}')

#icecreamstand1: IceCreamStand = IceCreamStand('gelatomangiato', 'ice cream', ['coconut', 'mango', 'strawberry'])
#icecreamstand1.describe_flavors()

#9-7
class Admin(User):

    def __init__(self, first_name: str, last_name: str, email: str, age: int, privileges: list) -> None:
        
        super().__init__(first_name, last_name, email, age)
        self.privileges = privileges

    def show_privileges(self):

        print('Privileges:')
        for privilege in self.privileges:
            print(privilege)

#admin1: Admin = Admin('Momo', 'Gogo', 'mogo@gmail.com', 23, ["can add post", "can delete post", "can ban user"])
#admin1.show_privileges()

#9-8
class Admin(User):

    def __init__(self, first_name: str, last_name: str, email: str, age: int, privileges: object) -> None:
        
        super().__init__(first_name, last_name, email, age)
        self.privileges = privileges

class Privileges:

    def __init__(self, privileges: list) -> None:
        
        self.privileges = privileges

    def show_privileges(self):

        print('Privileges:')
        for privilege in self.privileges:
            print(privilege)
    
#privileges1: Privileges = Privileges(["can add post", "can delete post", "can ban user"])
#admin2: Admin = Admin('Giorgio', 'Gialli', 'giogia@gmail.com', 53, privileges1)
#admin2.privileges.show_privileges()

#9-9
class Electric_Car:

    def __init__(self, brand: str, plate: str, battery: object) -> None:
        
        self.brand = brand
        self.plate = plate
        self.battery = battery
        self.range = battery.size * battery.capacity

    def get_range(self):

        return self.battery.size * self.battery.capacity

class Battery:

    def __init__(self, size: float, capacity: int) -> None:
        
        self.size = size
        self.capacity = capacity
    
    def upgrade_battery(self):

        if (self.capacity < 65):
            
            self.capacity = 65
   
#battery1: Battery = Battery(40.0, 30)
#elec_car1: Electric_Car = Electric_Car('Tesla', '123rtv765', battery1)
#read1 = elec_car1.get_range()
#print(read1)
#elec_car1.battery.upgrade_battery()
#read1 = elec_car1.get_range()
#print(read1)

#9-10
#risto_import: Restaurant_import = Restaurant_import('Mammt', 'Napoletana')
#risto_import.describe_restaurant_import()

#9-11
