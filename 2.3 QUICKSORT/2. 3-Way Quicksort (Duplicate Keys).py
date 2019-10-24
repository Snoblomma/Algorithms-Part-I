import unittest
import random

class TestDuplicateKeys(unittest.TestCase):
    def testChars(self):
        toSortList = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E'] 
        sortedList = ['A', 'C', 'E', 'E', 'I', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X']
        sortDuplicateKeys = ThreeWayQuicksort(toSortList)
        self.assertEqual(sortDuplicateKeys.result, sortedList)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortDuplicateKeys = ThreeWayQuicksort(toSort)
        self.assertEqual(sortDuplicateKeys.result, sort)

    def testDuplicates(self):
        toSort = ['R', 'B', 'W', 'W', 'R', 'W', 'B', 'R', 'R', 'W', 'B', 'R']
        sort = ['B', 'B', 'B', 'R', 'R', 'R', 'R', 'R', 'W', 'W', 'W', 'W']
        sortDuplicateKeys = ThreeWayQuicksort(toSort)
        self.assertEqual(sortDuplicateKeys.result, sort)

class ThreeWayQuicksort(object):
    result = []

    def __init__(self, a):
        random.shuffle(a)
        self.sort(a, 0, len(a) - 1)
        self.result = a

    def sort(self, a, lo=int, hi=int):
        if hi <= lo:
            return
        lt = lo
        gt = hi
        v = a[lo]
        i = lo
        while i <= gt:
            # cmp = a[i].compareTo(v)
            if (a[i] < v):
                a[lt], a[i] = a[i], a[lt]
                lt+=1
                i+=1
            elif (a[i] > v):
                a[i], a[gt] = a[gt], a[i]
                gt -= 1
            else:
                i+=1

        self.sort(a, lo, lt - 1)
        self.sort(a, gt + 1, hi)
        

if __name__ == "__main__":
    unittest.main()