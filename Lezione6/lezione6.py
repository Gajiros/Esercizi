class Person:
    def __init__(self, name: str, surname: str, ssn: str, birth_date: str, birth_place: str, gender: str) -> None:
        
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
        This function checks if the ssn is right
        input = None
        return = 
        '''
        
    
    def __str__(self) -> str:
        return f'Name: {self._name}, Surname: {self._surname}, Ssn: {self._ssn}.'

persona1: Person = Person(name = 'Gabriel', surname = 'Jimenez', ssn = 'nonloso')
persona2: Person = Person(name = 'Valentina', surname = 'Rossi', ssn = 'idk')
#print(persona1.get_name())
queue: list[Person] = [persona1, persona2]
print(str(persona1))
#for read in queue:

#    print(read.get_ssn())

#persona1.set_name(name = 'Gianni')
persona1.set_ssn('dio')
print(str(persona1))
#print(persona1.get_name())