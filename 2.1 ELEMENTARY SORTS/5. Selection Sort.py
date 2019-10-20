import unittest

class TestSelectionSort(unittest.TestCase):
    def testChars(self):
        toSort = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X']
        sortedArray = SelectionSort(toSort)
        self.assertEqual(sortedArray.result, sort)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = SelectionSort(toSort)
        self.assertEqual(sortedArray.result, sort)

class SelectionSort(object):
    result = []

    def __init__(self, toSort):
        N = len(toSort)
        
        for i in range(N):
            m = i
            for j in range(i, N):
                if toSort[j] < toSort[m]:
                    m = j
            toSort[i], toSort[m] = toSort[m], toSort[i]
        
        self.result = toSort

if __name__ == "__main__":
    unittest.main()