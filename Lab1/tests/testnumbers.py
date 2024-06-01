import unittest

from number import Number
from binarithmetic import plus, minus, multiplication, division, float_plus
from float import Float
from fixdotnumber import FixDotNumber

class TestNumbers(unittest.TestCase):

    def setUp(self):

        self.number1 = Number(4)
        self.number2 = Number(2)
        self.float1 = Float(3.2)
        self.float2 = Float(4.7)

    def test_plus(self):
        
        result = Number(6)
        sum = plus(self.number1, self.number2)

        self.assertEqual(sum.get_dec(), result.get_dec())
        self.assertEqual(sum.get_bin_sign(), result.get_bin_sign())
        self.assertEqual(sum.get_bin_ones_complement(), result.get_bin_ones_complement())
        self.assertEqual(sum.get_bin_twos_complement(), result.get_bin_twos_complement())

    def test_minus(self):
        
        result = Number(2)
        dif = minus(self.number1, self.number2)

        self.assertEqual(dif.get_dec(), result.get_dec())
        self.assertEqual(dif.get_bin_sign(), result.get_bin_sign())
        self.assertEqual(dif.get_bin_ones_complement(), result.get_bin_ones_complement())
        self.assertEqual(dif.get_bin_twos_complement(), result.get_bin_twos_complement())

    def test_multi(self):
        
        result = Number(8)
        multi = multiplication(self.number1, self.number2)

        self.assertEqual(multi.get_dec(), result.get_dec())
        self.assertEqual(multi.get_bin_sign(), result.get_bin_sign())
        self.assertEqual(multi.get_bin_ones_complement(), result.get_bin_ones_complement())
        self.assertEqual(multi.get_bin_twos_complement(), result.get_bin_twos_complement())

    def test_division(self):
        
        result = FixDotNumber(2.0)
        div = division(self.number1, self.number2)

        self.assertEqual(str(div), str(result))

    def test_plus_float(self):
        
        result = Float(7.9)
        sum = float_plus(self.float1, self.float2)

        self.assertAlmostEqual(sum.get_value(), result.get_value(), delta=10**(-3))
        self.assertEqual(sum.get_mantissa(), result.get_mantissa())
        self.assertEqual(sum.get_exponent(), result.get_exponent())
        
if __name__ == "__main__":
    unittest.main()

