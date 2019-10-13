#An N2 log N algorithm for 3-SUM

import unittest

class TestThreeSum(unittest.TestCase):
    def test(self):
        threeSum = ThreeSum()
        f = open('/home/kate/Documents/Algorithms Part I/Algorithms-Part-I/1.4 ANALYSIS OF ALGORITHMS/8ints.txt')
        a = list(map(int,f.readline().split(' '))) 
        self.assertEqual(threeSum.count(a), 4)   

class ThreeSum:
    def count(self, a):
        N = len(a)
        a.sort()
        count = 0
        for i in range(N):
            for j in range(i + 1, N):           
                toFind = -1*(a[i] + a[j])
                if self.binarySearch(a[(j+1):], toFind) > -1:
                    count += 1
        return count

    def binarySearch(self, a, key):
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