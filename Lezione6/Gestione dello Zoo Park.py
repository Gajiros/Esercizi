class Zoo:
    
    def __init__(self, fence: list, zoo_keeper: list) -> None:
        
        self.fence = fence
        self.zoo_keeper = zoo_keeper
    
    def describe_zoo(self):
        
        print('\nGuardians:')
        for read in self.zoo_keeper:
            print(f'Name: {read.name} | Surname: {read.surname} | Id: {read.id}\n')
        print('Fences:')
        for read in self.fence:
                print(f'Area: {read.area} | Temperature: {read.temperature} | Habitat: {read.habitat}')
                for animal in read.animal:
                    print(str(animal))
                print('##############################')

class Fence:
    
    def __init__(self, animal: list, area: float, temperature: float, habitat: str) -> None:
        
        self.animal = animal
        self.area = area
        self.temperature = temperature
        self.habitat = habitat

class Animal:
    
    def __init__(self, name: str, species: str, age: int, height: float, width: float, preferred_habitat: str) -> None:
        
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)
        self.fence = None

    def __str__(self) -> str:
        return f'Animal(Name: {self.name} | Species: {self.species} | Age: {self.age})'

class Zoo_Keeper:
    
    def __init__(self, name: str, surname: str, id: str) -> None:
        
        self.name = name
        self.surname = surname
        self.id = id
    
    def add_animal(self, animal: Animal, fence: Fence):
        
        if (animal.preferred_habitat == fence.habitat) and ((fence.area - (animal.width * animal.height)) >= 0):
            fence.animal.append(animal)
            fence.area -= (animal.width * animal.height)
            animal.fence = fence
            print('The animal has been added.')
        else:
            print('The habitat isn\'t the best for this animal.')

    def remove_animal(self, animal: Animal, fence: Fence):

        fence.animal.remove(animal)
        fence.area += (animal.width * animal.height)
        print('The animal has been removed.')

    def feed(self, animal: Animal):
        if (animal.fence.area - (((animal.height * 2) / 100) * ((animal.width * 2) / 100)) >= 0):
            animal.health += animal.health / 100
            animal.height += (animal.height * 2) / 100
            animal.width += (animal.width * 2) / 100
            print('The animal has been fed.')
        else:
            print('The area of the fence ins\'t big enough.')
    
    def clean(self, fence: Fence) -> float:
        time: float = 0
        area_occupied: float = 0
        if (fence.area == 0):
            for read in fence.animal:
                time += (read.height * read.width)
            return time
        else:
            for read in fence.animal:
                area_occupied += (read.height * read.width)
            time += (area_occupied / fence.area)
            return time

