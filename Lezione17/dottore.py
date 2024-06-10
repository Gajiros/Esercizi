from persona import Persona

class Dottore(Persona):

    def __init__(self, first_name: str, last_name: str, specialization: str, parcel: float) -> None:
        super().__init__(first_name, last_name)
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            print('La spacializzazione inserita non è una stringa!')
            self.specialization = None
        
        if isinstance(parcel, int):
            self.parcel = parcel
        else:
            print('La parcella inserita non è un intero!')
            self.parcel = None

    def setSpecialization(self, specialization: str):
        if isinstance(specialization, str):
            self.specialization = specialization
        else:
            print('La spacializzazione inserita non è una stringa!')
    
    def setParcel(self, parcel: int):
        if isinstance(parcel, int):
            self.parcel = parcel
        else:
            print('La parcella inserita non è un intero!')
    
    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self) -> bool:
        if (self.age > 30):
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
            return True
        else:
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
            return False

    def doctorGreet(self):
        Persona.greet(self)
        print(f'Sono un medico {self.specialization}')