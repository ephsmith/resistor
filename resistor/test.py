from unittest import TestCase
from resistor import Resistance, Resistor

class TestResistance(TestCase):
    """ Tests for the Resistance class """

    def test_prop_resistance(self):
        ''' Test the resistance property '''
        r = Resistance(1000)
        self.assertEqual(1000, r.resistance)

    def test_prop_si(self):
        ''' Test the si property '''
        r = Resistance(1000)
        self.assertEqual('1.0 k', r.si)

    def test_precision_2(self):
        ''' test for two digits of precision '''
        r = Resistance(1000, precision=2)
        self.assertEqual('1.00 k', r.si)

    def test_mega(self):
        ''' test with a value with exponent +6 '''
        r = Resistance(1000000)
        self.assertEqual('1.0 M', r.si)

    def test_milli(self):
        ''' test with a value with exponent -3 '''
        r = Resistance(0.001)
        self.assertEqual('1.0 m', r.si)

class TestResistor(TestCase):
    ''' Test for the Resistor class '''

    params_codes = [ (1000, tuple('brown black red gold'.split())),
                     (1100, tuple('brown brown red gold'.split())),
                     (1200, tuple('brown red red gold'.split())),
                     (1300, tuple('brown orange red gold'.split())),
                     (1400, tuple('brown yellow red gold'.split())),
                     (1500, tuple('brown green red gold'.split())),
                     (1600, tuple('brown blue red gold'.split())),
                     (1700, tuple('brown purple red gold'.split())),
                     (1800, tuple('brown gray red gold'.split())),
                     (1900, tuple('brown white red gold'.split())),
                     (10, tuple('brown black black gold'.split())),
                     (100, tuple('brown black brown gold'.split())),
                     (10000, tuple('brown black orange gold'.split())),
                     (100000, tuple('brown black yellow gold'.split())),
                     (1000000, tuple('brown black green gold'.split())),
    ]


    def test_property_resistance(self):
        r = Resistor(resistance=1000) #default tolerance of 0.05
        self.assertEqual(1000, r.resistance)

    def test_property_code(self):
        r = Resistor(resistance=1000)
        self.assertEqual( ('brown', 'black', 'red', 'gold'), r.code)

    def test_codes(self):
        for param, code in self.params_codes:
            with self.subTest():
                r = Resistor(resistance=param)
                self.assertEqual(code, r.code)


if __name__ == '__main__':
    unittest.main()
