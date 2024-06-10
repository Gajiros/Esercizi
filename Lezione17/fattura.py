from dottore import Dottore

class Fattura:

    def __init__(self, patients: list, doctor: object) -> None:
        counter: int = 0
        for patient in patients:
            counter += 1
        if (Dottore.isAValidDoctor == True):
            self.fatture = counter
            self.salary = 0
            self.patients = patients
            self.doctor = doctor
        else:
            self.fatture = None
            self.salary = None
            self.patients = None
            self.doctor = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        self.salary = self.doctor.getParcel() * self.getFatture
        return self.salary

    def getFatture(self):
        counter: int = 0
        for patient in self.patients:
            counter += 1
        self.fatture = counter
        return self.fatture

    def addPatient(self, newPatient: object):
        self.patients.append(newPatient)
        self.getFatture()
        self.getSalary()
        print(f'Alla lista del Dottor {self.doctor.last_name} è stato aggiunto il paziente {newPatient.idCode}')
    
    def removePatient(self, id: str):
        for patient in self.patients:
            if(patient.idCode == id):
                print(f'lla lista del Dottor {self.doctor.last_name} è stato rimosso il paziente {patient.idCode}')
                self.patients.remove(patient)
                self.getFatture()
                self.getSalary()