import unittest
import random

class TestShellsort(unittest.TestCase):
    def testChars(self):
        array = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        shuffledArray = Shuffle(a)
        self.assertNotEqual(shuffledArray.result, array)

    def testInts(self):
        array = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        a = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        shuffledArray = Shuffle(a)
        self.assertNotEqual(shuffledArray.result, array)

class Shuffle(object):
    result = []

    def __init__(self, a):
        N = len(a)
        for i in range(N):
            r = random.uniform(0, i+1)
            a[i], a[int(r)] = a[int(r)], a[i]
        self.result = a

if __name__ == "__main__":
    unittest.main()