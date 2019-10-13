import unittest

class TestBinarySearch(unittest.TestCase):
    def testSearch(self):
        a = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97]
        self.assertEqual(binarySearch(a, 33), 4)   
        self.assertEqual(binarySearch(a, 5), -1)   


def binarySearch(a, key):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo)/2)
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid 
    return -1

if __name__ == '__main__':
    unittest.main()
    # a = list(map(int,input().split(' '))) 
    # key = int(input())
    # print(binarySearch(a, key))