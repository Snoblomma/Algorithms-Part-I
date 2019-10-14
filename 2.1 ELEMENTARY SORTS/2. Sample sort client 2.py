# Sort strings from file in alphabetical order
import random
import unittest

class TestStringSorter(unittest.TestCase):
    def test_connect(self):
        a = ['bed', 'bug', 'dad', 'yet', 'zoo', 'all', 'bad', 'yes']
        sorted_a = ['all', 'bad', 'bed', 'bug', 'dad', 'yes', 'yet', 'zoo']
        stringSorter = StringSorter()
        self.assertEqual(stringSorter.sort(a), sorted_a)

class StringSorter:

    def sort(self, a):
        return(sorted(a))


if __name__ == '__main__':
    unittest.main()