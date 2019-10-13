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
        count = 0
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if a[i] + a[j] + a[k] == 0:
                        count += 1
        return count



if __name__ == '__main__':
    unittest.main()
    # a = list(map(int,input().split(' '))) 
    # ThreeSum.count(a)