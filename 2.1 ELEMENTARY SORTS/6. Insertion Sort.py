import unittest

class TestInsertionSort(unittest.TestCase):
    def testChars(self):
        toSort = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X']
        sortedArray = InsertionSort(toSort)
        self.assertEqual(sortedArray.result, sort)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = InsertionSort(toSort)
        self.assertEqual(sortedArray.result, sort)

class InsertionSort(object):
    result = []

    def __init__(self, a):
        N = len(a)
        
        for i in range(N):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
                else:
                    break
        
        self.result = a

if __name__ == "__main__":
    unittest.main()