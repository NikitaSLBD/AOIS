import unittest
from logical_expression import LogicalExpression
from truth_table import get_truth_table
from forms import build_sdnf, build_sknf, index_form

class TestLogicalExpression(unittest.TestCase):

    def setUp(self):
        self.logic_expression = LogicalExpression("(a|!b&a->b)~b")

    def test_init(self):
        self.assertEqual(str(self.logic_expression), "(a|!b&a→b)~b")
        self.assertEqual(self.logic_expression.get_variables(), ['a', 'b'])

    def test_get_truth_table(self):
        
        truth_table = get_truth_table(self.logic_expression)

        self.assertEqual(next(truth_table), ({'a': 0, 'b': 0}, {'!b': 1, 'a|!b': 1, 'a|!b&a': 0, 'a|!b&a→b': 1, 'a|!b&a→b~b': 0}))
        self.assertEqual(next(truth_table), ({'a': 0, 'b': 1}, {'!b': 0, 'a|!b': 0, 'a|!b&a': 0, 'a|!b&a→b': 1, 'a|!b&a→b~b': 1}))
        self.assertEqual(next(truth_table), ({'a': 1, 'b': 0}, {'!b': 1, 'a|!b': 1, 'a|!b&a': 1, 'a|!b&a→b': 0, 'a|!b&a→b~b': 1}))
        self.assertEqual(next(truth_table), ({'a': 1, 'b': 1}, {'!b':0, 'a|!b': 1, 'a|!b&a': 1, 'a|!b&a→b': 1, 'a|!b&a→b~b': 1}))

    def test_build_sdnf(self):
        sdnf = build_sdnf(get_truth_table(self.logic_expression))
        expected_output = {'(!a&b)|(a&!b)|(a&b)': [1, 2, 3]}
        self.assertEqual(sdnf, expected_output)

    def test_build_sknf(self):
        sknf = build_sknf(get_truth_table(self.logic_expression))
        expected_output = {'(a|b)': [0]}
        self.assertEqual(sknf, expected_output)

    def test_index_form(self):
        index = index_form(get_truth_table(self.logic_expression))
        expected_output = {7: '0111'}
        self.assertEqual(index, expected_output)


if __name__ == '__main__':
    unittest.main()

        


