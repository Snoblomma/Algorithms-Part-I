import unittest
import random 

class TestQuicksort(unittest.TestCase):
    def testChars(self):
        toSortList = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E'] 
        sortedList = ['A', 'C', 'E', 'E', 'I', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'X']
        quicksort = Quicksort(toSortList)
        self.assertEqual(quicksort.result, sortedList)
    
    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = Quicksort(toSort)
        self.assertEqual(sortedArray.result, sort)

class Quicksort(object):
    result = []

    def __init__(self, a):
        random.shuffle(a)
        self.sort(a, 0, len(a) - 1)
        self.result = a

    def partition(self, a, lo=int, hi=int):
        i = lo
        j = hi+1

        while True:
            i+=1
            while a[i] < a[lo]:
                if i == hi:
                    break
                i+=1

            j-=1
            while a[lo] < a[j]:
                if j == lo:
                    break
                j-=1

            if i >= j:
                break
            a[i], a[j] = a[j], a[i]

        a[lo], a[j] = a[j], a[lo]
        return j

    def sort(self, a,lo=int, hi=int):
        if hi <= lo:
            return
        j = self.partition(a, lo, hi)
        self.sort(a, lo, j-1)
        self.sort(a, j+1, hi)

if __name__ == "__main__":
    unittest.main()