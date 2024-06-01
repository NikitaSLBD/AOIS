import unittest
import sys
from io import StringIO

from hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.table = HashTable()
        self.small_table = HashTable(3)

    def test_init(self):
        self.assertEqual(len(self.small_table), 3)
        self.assertEqual(len(self.table), 20)
        
    def test_add_get(self):
        self.table.add('A', 'first letter')
        self.assertEqual(self.table.get('A'), 'first letter')

    def test_upd(self):
        self.table.add('B', 'second letter')
        self.table.upd('B', 'capital letter "b"')
        self.assertEqual(self.table.get('B'), 'capital letter "b"')

    def test_rem(self):
        self.table.add('C', 'third letter')
        self.table.rem('C')

        self.assertEqual(self.table.get('C'), None)


    def test_write(self):
        
        output = StringIO()
        sys.stdout = output

        self.small_table.write()

        sys.stdout = sys.__stdout__
        message = "0 None\n1 None\n2 None\n"

        self.assertEqual(output.getvalue(), message)
        
if __name__ == '__main__':
    unittest.main()