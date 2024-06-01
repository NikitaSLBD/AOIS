import unittest

from minimization import calculate_minimization, table_minimization, carno_minimization


class TestMinimization(unittest.TestCase):

    def setUp(self):

        self.logic_expression = "(a|b)&(a|!b)"
        self.calculate_min = calculate_minimization
        self.table_min = table_minimization
        self.carno_min = carno_minimization

    def test_calculate_minimization_(self):
        self.assertEqual(self.calculate_min(self.logic_expression), '(a)')

    def test_table_minimization_(self):
        self.assertEqual(self.table_min(self.logic_expression), '(a)')

    def test_carno_minimization(self):
        self.assertEqual(self.carno_min(self.logic_expression), '(a)')

if __name__ == '__main__':
    unittest.main()