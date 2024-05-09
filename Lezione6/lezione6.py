
class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._ssn: str = None
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender: str = gender
        self.compute_ssh
    
    def get_name(self):
        '''
        This function returns the person's name\n
        input = None\n
        return = self._name: str
        '''

        return self._name
    
    def set_name(self, name: str):
        '''
        This function sets the attribute's name
        input = self._name: str
        return = None
        '''
        raise Exception('You cannot modify the name.')
    
    def get_ssn(self):
        '''
        This function returns the person's ssn\n
        input = None\n
        return = self._ssn: str
        '''

        return self._ssn
    
    def set_ssn(self, ssn: str):
        '''
        This function sets the person's ssn
        input = self._ssn: str
        return = None
        '''
        raise Exception('You cannot change the ssn.')

    def compute_ssh(self) -> None:
        '''
        This function computes the ssn
        input = None
        return = str
        '''
        first_3_consonants_surname: str = ''
        vocals: str = 'aeiou'
        for read in self._surname:
            flag1: bool = False
            if (len(first_3_consonants_surname) < 3):
                for read2 in vocals:
                    if (read != read2):
                        continue
                    else:
                        flag1 = True
                        break
                if (flag1 == True):
                    continue
                else:
                    first_3_consonants_surname += read
            else:
                break
        print(first_3_consonants_surname)
                        
    def __str__(self) -> str:
        return f'Name: {self._name}, Surname: {self._surname}, Ssn: {self._ssn}.'

person1: Person = Person(name = 'Gabriel', surname = 'Jimenez', birth_date = '30\\05\\2004', birth_place = 'Rome', gender = 'M')
person1.compute_ssh()
#persona2: Person = Person(name = 'Valentina', surname = 'Rossi', ssn = 'idk')
#print(persona1.get_name())
#queue: list[Person] = [persona1, persona2]
#print(str(persona1))
#for read in queue:

#    print(read.get_ssn())

#persona1.set_name(name = 'Gianni')
#persona1.set_ssn('dio')
#print(str(persona1))
#print(persona1.get_name())
"""
#Exercise 2 
class Student:
    def __init__(self, name: str, studyProgram: str, age: str, gender: str) -> None:
        
        self.name: str = name
        self.studyProgram: str = studyProgram
        self.age: str = age
        self.gender: str = gender
    
    def printInfo(self) -> None:

        print(f'Name: {self.name} | Study Program: {self.studyProgram} | Age: {self.age} | Gender: {self.gender}.')

student1: Student = Student('Gabriel', 'Python', 19, 'Male')
student2: Student = Student('Valerio', 'Python', 45, 'Male')
student3: Student = Student('Momo', 'Python', 89, 'Transexual Female')
student1.printInfo()
student2.printInfo()
student3.printInfo()

#Exercise 3
class Animal:
    def __init__(self, name: str, weight: float, legs: int) -> None:
        
        self.name: str = name
        self.weight: float = weight
        self.legs: int = legs
    
    def setLegs(self, legs):

        self.legs = legs

    def getLegs(self):

        return self.legs

    def printInfo(self):

        print(f'Name: {self.name} | Weight: {self.weight} | Legs: {self.legs}')

animal1: Animal = Animal('Topo Gigio', 3.0, 4)
animal2: Animal = Animal('Paperino', 7.0, 5)
animal1.legs = 9
animal1.setLegs(10)
print(animal1.getLegs())
animal1.printInfo()

class Food:
    def __init__(self, name: str, price: float, description: str) -> None:
        
        self.name: str = name
        self.price: float = price
        self.description: str = description

class Menu:

    def __init__(self, food: list = []) -> None:
    
        self.food_list: list = food
    
    def addFood(self, food: Food) -> None:
        
        self.food_list.append(food)
    
    def removeFood(self, food: Food) -> None:

        self.food_list.remove(food)
        
    def printPrices(self) -> None:

        for read in self.food_list:
            print(read.price)
    
    def getAvaragePrice(self) -> float:
        
        sum: float = 0
        COUNT: int = 0
        for read in self.food_list:
            sum += read.price
            COUNT += 1
        return sum / COUNT

food1: Food = Food('Watermelon', 0.90, 'Fruit')
food2: Food = Food('Pasta', 1.20, 'Fusilli')
food3: Food = Food('Tomato', 1.70, 'Vegetable')
food4: Food = Food('Pesto', 2.40, 'Sauce')
food5: Food = Food('Meat', 7.60, 'Cow Meat')
menu1: Menu = Menu([food1, food2])
menu1.addFood(food4)
menu1.removeFood(food1)
menu1.printPrices()
print(menu1.getAvaragePrice())
"""