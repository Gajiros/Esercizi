import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

class TestPersona(unittest.TestCase):

    def setUp(self) -> None:
        self.persona: Persona = Persona('Valerio', 'Rondoni')
    
    def testMetodi(self):
        self.assertEqual(self.persona.getName(), 'Valerio')
        self.persona.setName('Gabriel')
        self.assertEqual(self.persona.getName(), 'Gabriel')
        self.assertEqual(self.persona.getLastName(), 'Rondoni')
        self.persona.setLastName('Jimenez')
        self.assertEqual(self.persona.getLastName(), 'Jimenez')
        self.assertEqual(self.persona.getAge(), 0)
        self.persona.setAge(20)
        self.assertEqual(self.persona.getAge(), 20)

class TestDottore(unittest.TestCase):

    def setUp(self):
        self.dottore: Dottore = Dottore('Gianluca', 'Vizconde', 'Fisioterapista', 50.0)
    
    def testMetodi(self):
        self.assertEqual(self.dottore.getSpecialization(), 'Fisioterapista')
        self.dottore.setSpecialization('Chirurgo')
        self.assertEqual(self.dottore.getSpecialization(), 'Chirurgo')
        self.assertEqual(self.dottore.getParcel(), 50.0)
        self.dottore.setParcel(45.0)
        self.assertEqual(self.dottore.getParcel(), 45.0)
        self.assertEqual(self.dottore.isAValidDoctor(), False)
        self.dottore.setAge(40)
        self.assertEqual(self.dottore.isAValidDoctor(), True)

class TestPaziente(unittest.TestCase):

    def setUp(self) -> None:
        self.paziente: Paziente = Paziente('Edoardo', 'Cremonesi', 'ec20')

    def testMetodi(self):
        self.assertEqual(self.paziente.getIdCode(), 'ec20')
        self.paziente.setIdCode('ec2023')
        self.assertEqual(self.paziente.getIdCode(), 'ec2023')

class TestFattura(unittest.TestCase):

    def setUp(self) -> None:
        paziente1: Paziente = Paziente('Edoardo', 'Cremonesi', 'ec20')
        dottore2: Dottore = Dottore('Gabriel', 'Jimenez', 'Vincitore', '666')
        dottore2.setAge(40)
        self.fattura: Fattura = Fattura([paziente1], dottore2)

    def testMetodi(self):
        paziente2: Paziente = Paziente('Valerio', 'Rondoni', 'vr20')
        self.assertEqual(self.fattura.getFatture(), 1)
        self.assertEqual(self.fattura.getSalary(), 666.0)
        self.fattura.addPatient(paziente2)
        self.assertEqual(self.fattura.getFatture(), 2)
        self.assertEqual(self.fattura.getSalary(), 1332.0)
        self.fattura.removePatient('vr20')
        self.assertEqual(self.fattura.getFatture(), 1)
        self.assertEqual(self.fattura.getSalary(), 666.0)

if __name__ == '__main__':
    unittest.main() 