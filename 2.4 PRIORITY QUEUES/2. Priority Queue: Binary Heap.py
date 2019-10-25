import unittest

def removeNones(a):
    return [i for i in a if i] 

class TestPriorityMaxPQ(unittest.TestCase):
    def test(self):
        t = MaxPQ(7)
        t.insert('P')
        t.insert('Q')
        t.insert('E')
        t.delMax()
        t.insert('X')
        t.insert('A')
        t.insert('M')
        t.delMax()
        t.insert('P')
        t.insert('L')
        t.insert('E')
        t.delMax()
        self.assertEqual(sorted(removeNones(t.pq)), ['A', 'E', 'L', 'M', 'P'])


class MaxPQ(object):
    pq = None
    N = 0

    def __init__(self, capacity=int):
        self.pq = [None]*int(capacity+1)

    def isEmpty(self):
        return self.N == 0

    def less(self, a, b):
        if a is not None and b is not None:
            if a < b:
                return True
            else:
                return False
        elif a and b is None:
            return False
        elif a is None:
            return False
        elif b is None:
            return True
        else:
            return False

    def swim(self, k=int):
        while k > 1 and self.less(int(k/2), k):
            self.pq[int(k)], self.pq[int(k/2)] = self.pq[int(k/2)], self.pq[int(k)]
            k = k/2

    def sink(self, k=int):
        while (2*k <= self.N):
            j = 2*k
            if j < self.N and self.less(j, j+1):
                j+=1
            if self.less(k, j) == False:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j
        
    def insert(self, x):
        self.N += 1
        self.pq[self.N] = x   
        self.swim(self.N)
        
    def delMax(self):
        m = self.pq[1]
        self.pq[1], self.pq[self.N-1] = self.pq[self.N-1], self.pq[1]
        self.sink(1)       
        self.pq[self.N-1] = None
        self.N -= 1
        return m


if __name__ == "__main__":
    unittest.main()