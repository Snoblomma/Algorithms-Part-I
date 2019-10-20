import unittest

class TestSelectionSort(unittest.TestCase):
    def test(self):
        toSort = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'M', 'P', 'L', 'E', 'E', 'R', 'O', 'S', 'T', 'X']
        sortedArray = SelectionSort(toSort)
        self.assertEqual(sortedArray.result, sort)

class SelectionSort(object):
    result = []

    def __init__(self, toSort):
        N = len(toSort)
        
        for i in range(N):
            min = i
            for j in range(i+1, N):
                if toSort[j] < toSort[min]:
                    min = j
                    toSort[i], toSort[min] = toSort[min], toSort[i]
        
        self.result = toSort

if __name__ == "__main__":
    unittest.main()