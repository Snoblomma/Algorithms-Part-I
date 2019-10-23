import unittest
import math

class TestMergesortBU(unittest.TestCase):
    def testChars(self):
        toSort = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'E', 'E', 'E', 'E', 'G', 'L', 'M', 'M', 'O', 'P', 'R', 'R', 'S', 'T', 'X']
        sortedArray = MergesortBU(toSort)
        self.assertEqual(sortedArray.result, sort)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = MergesortBU(toSort)
        self.assertEqual(sortedArray.result, sort)

class MergesortBU(object):
    result = []

    def __init__(self, a):
        self.sort(a)

    def merge(self, a, aux, lo=int, mid=int, hi=int):
        assert (sorted(a[lo:mid+1]) == a[lo:mid+1]), 'Array not sorted'
        assert (sorted(a[mid+1:hi+1]) == a[mid+1:hi+1]), 'Array not sorted'

        for k in range(lo, hi+1):
            aux[k] = a[k]

        i = lo
        j = mid+1

        for k in range(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j+=1
            elif j > hi:
                a[k] = aux[i]
                i+=1
            elif aux[j] < aux[i]:
                a[k] = aux[j]
                j+=1
            else:
                a[k] = aux[i]
                i+=1

        assert (sorted(a[lo:hi+1]) == a[lo:hi+1]), 'Array not sorted'
        self.result = a

    def sort(self, a):
        N = len(a)
        aux = [None]*N
        
        sz = 1
        while sz < N:
            for lo in range(0, N-sz, sz+sz):
                self.merge(a, aux, lo, lo+sz-1, min(lo+sz+sz-1, N-1))
            sz = sz+sz
            



if __name__ == "__main__":
    unittest.main()