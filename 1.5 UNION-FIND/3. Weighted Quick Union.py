import unittest

class TestStringMethods(unittest.TestCase):
    def test_connect(self):
        quickUnion = QuickUnion(12)
        self.assertEqual(quickUnion.connected(3, 4), False)
        quickUnion.union(4, 3)
        self.assertEqual(quickUnion.connected(3, 4), True)

    def test_connect_reflexive(self):
        quickUnion = QuickUnion(12)
        self.assertEqual(quickUnion.connected(3, 3), True)

    def test_connect_symmetric(self):
        quickUnion = QuickUnion(12)
        quickUnion.union(4, 3)
        self.assertEqual(quickUnion.connected(3, 4), True)
        self.assertEqual(quickUnion.connected(4, 3), True)

    def test_connect_transitive(self):
        quickUnion = QuickUnion(12)
        quickUnion.union(1, 2)
        quickUnion.union(2, 6)
        self.assertEqual(quickUnion.connected(1, 6), True)

    def test_connect_2(self):
        quickUnion = QuickUnion(12)   
        quickUnion.union(4, 3)
        quickUnion.union(3, 8)
        quickUnion.union(6, 5)
        quickUnion.union(9, 4)
        quickUnion.union(2, 1)
        self.assertEqual(quickUnion.connected(0, 7), False)
        self.assertEqual(quickUnion.connected(8, 9), True)
        quickUnion.union(5, 0)
        quickUnion.union(7, 2)
        quickUnion.union(6, 1)
        quickUnion.union(1, 0)
        self.assertEqual(quickUnion.connected(0, 7), True)

class QuickUnion:
    id = []
    sz = []

    def __init__ (self, n):
        self.id = [None]*n
        self.sz = [0]*n
        for i in range(n):
            self.id[i] = i
    
    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i != j:
            if self.sz[i] < self.sz[j]:
                self.id[i] = j; 
                self.sz[j] += self.sz[i]; 
            else:
                self.id[j] = i
                self.sz[i] += self.sz[j]


if __name__ == '__main__':
    unittest.main()