import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        self.persona: Persona = Persona('Valerio', 'Rondoni')
    
    def testMetodi(self):
        self.assertEqual(self.persona.getName(), 'Valerio', 'Error')
        self.persona.setName('Gabriel')
        self.assertEqual(self.persona.getName(), 'Gabriel', 'Error')
        self.assertEqual(self.persona.getLastName(), 'Rondoni', 'Error')
        self.persona.setLastName('Jimenez')
        self.assertEqual(self.persona.getLastName(), 'Jimenez', 'Error')
        self.assertEqual(self.persona.getAge(), 0, 'Error')
        self.persona.setAge(20)
        self.assertEqual(self.persona.getAge(), 20, 'Error')
        self.assertEqual(self.persona.greet(), 'Ciao, sono Gabriel Jimenez! Ho 20 anni!', 'Error')

class TestDottore(unittest.TestCase):

    def setUp(self):
        self.dottore: Dottore = Dottore('Gianluca', 'Vizconde', 'Fisioterapista', 50)
    
    def testMetodi(self):
        self.assertEqual(self.dottore.getSpecialization(), 'Fisioterapista', 'Error')
        self.dottore.setSpecialization('Chirurgo')
        self.assertEqual(self.dottore.getSpecialization(), 'Chirurgo', 'Error')
        self.assertEqual(self.dottore.getParcel(), 50, 'Error')
        self.dottore.setParcel(45)
        self.assertEqual(self.dottore.getParcel(), 45, 'Error')
        self.assertEqual(self.dottore.isAValidDoctor(), False, 'Error')
        self.dottore.setAge(40)
        self.assertEqual(self.dottore.isAValidDoctor(), True, 'Error')
        self.assertEqual(self.dottore.doctorGreet(), 'Sono un medico Chirurgo', 'Error')

class TestPaziente(unittest.TestCase):

    def setUp(self) -> None:
        self.paziente: Paziente = Paziente('Edoardo', 'Cremonesi', 'ec20')

    def testMetodi(self):
        self.assertEqual(self.paziente.getIdCode(), 'ec20', 'Error')
        self.paziente.setIdCode('ed2023')
        self.assertEqual(self.paziente.getIdCode(), 'ec2023', 'Error')
        self.assertEqual(self.paziente.patientInfo(), 'Paziente: Edoardo Cremonesi\nID: ec2023', 'Error')

class TestFattura(unittest.TestCase):

    def setUp(self) -> None:
        paziente1: Paziente = Paziente('Edoardo', 'Cremonesi', 'ec20')
        dottore: Dottore = Dottore('Gabriel', 'Jimenez', 'Vincitore', '666')
        self.fattura: Fattura = Fattura([paziente1], dottore)

    def testMetodi(self):
        paziente2: Paziente = Paziente('Valerio', 'Rondoni', 'vr20')
        self.assertEqual(self.fattura.getFatture(), 1, 'Error')
        self.assertEqual(self.fattura.getSalary(), 666.0, 'Error')
        self.fattura.addPatient(paziente2)
        self.assertEqual(self.fattura.getFatture(), 2, 'Error')
        self.assertEqual(self.fattura.getSalary(), 1332.0, 'Error')
        self.fattura.removePatient('vr20')
        self.assertEqual(self.fattura.getFatture(), 1, 'Error')
        self.assertEqual(self.fattura.getSalary(), 666.0, 'Error')

if __name__ == '__main__':
    unittest.main() 