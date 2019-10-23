import unittest

class TestMergesort(unittest.TestCase):
    def testChars(self):
        toSort = ['M', 'E', 'R', 'G', 'E', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        sort = ['A', 'E', 'E', 'E', 'E', 'G', 'L', 'M', 'M', 'O', 'P', 'R', 'R', 'S', 'T', 'X']
        sortedArray = Mergesort(toSort)
        self.assertEqual(sortedArray.result, sort)

    def testInts(self):
        toSort = [7, 4, 5, 6, 1, 2, 7, 4, 2, 6, 1, 7, 5, 3, 4, 2]
        sort = [1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 6, 6, 7, 7, 7]
        sortedArray = Mergesort(toSort)
        self.assertEqual(sortedArray.result, sort)

class Insertion(object):

    def sort(self, a):
        N = len(a)
        
        for i in range(N):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    a[j], a[j-1] = a[j-1], a[j]
                else:
                    break
        return a

class Mergesort(object):
    result = []
    CUTOFF = 7

    def __init__(self, a):
        aux = [None]*len(a)
        self.sortArray(a, aux, 0, len(a)-1)

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

    def sortArray(self, a, aux, lo=int, hi=int):
        # Use insertion sort for small subarrays.
        if hi <= lo + self.CUTOFF - 1:
            a[lo:hi+1] = Insertion().sort(a[lo:hi+1])
            return

        if hi <= lo:
            return 

        mid = lo + (hi - lo) / 2
        self.sortArray(a, aux, lo, int(mid))
        self.sortArray(a, aux, int(mid)+1, hi)
        # Stop if already sorted.
        if a[int(mid)+1] > a[int(mid)]:
            return
        self.merge(a, aux, lo, int(mid), hi)


if __name__ == "__main__":
    unittest.main()