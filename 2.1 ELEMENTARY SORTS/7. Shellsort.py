import unittest

class TestShellsort(unittest.TestCase):
    def testChars(self):
        toSort = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X']
        sortedArray = Shellsort(toSort)
        self.assertEqual(sortedArray.result, sort)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = Shellsort(toSort)
        self.assertEqual(sortedArray.result, sort)

class Shellsort(object):
    result = []

    def __init__(self, a):
        N = len(a)
        h = 1

        while h < N/3:
            h = 3*h + 1

        while h >= 1:
            for i in range(int(h), N):
                j = i
                while j >= h and a[int(j)] < a[int(j-h)]:
                    a[int(j)], a[int(j-h)] = a[int(j-h)], a[int(j)]
                    j -= h

            h = int(h/3)
    
        self.result = a

if __name__ == "__main__":
    unittest.main()