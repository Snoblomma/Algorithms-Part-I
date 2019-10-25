import unittest

def removeNones(a):
    return [i for i in a if i] 

class TestPriorityQueueUnorderedArray(unittest.TestCase):
    def test(self):
        t = UnorderedMaxPQ(7)
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
        self.assertEqual(sorted(removeNones(t.pq)), ['A', 'E', 'E', 'L', 'M', 'P'])


class UnorderedMaxPQ(object):
    pq = None
    N = 0

    def __init__(self, capacity=int):
        self.pq = [None]*int(capacity)

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

    def insert(self, x):
        
        self.pq[self.N] = x
        self.N += 1
        
        
    def delMax(self):
        m = 0
        for i in range(1, self.N):
            if self.less(self.pq[m], self.pq[i]):
                m = i
                print('max ' + str(m))
       
        self.pq[m], self.pq[self.N-1] = self.pq[self.N-1], self.pq[m]
        self.pq[self.N - 1] = None
        self.N -= 1


if __name__ == "__main__":
    unittest.main()