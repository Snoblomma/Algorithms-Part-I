import unittest

class TestStringMethods(unittest.TestCase):
    def test_connect(self):
        quickFind = QuickFind(12)
        self.assertEqual(quickFind.connected(3, 4), False)
        quickFind.union(4, 3)
        self.assertEqual(quickFind.connected(3, 4), True)

    def test_connect_reflexive(self):
        quickFind = QuickFind(12)
        self.assertEqual(quickFind.connected(3, 3), True)

    def test_connect_symmetric(self):
        quickFind = QuickFind(12)
        quickFind.union(4, 3)
        self.assertEqual(quickFind.connected(3, 4), True)
        self.assertEqual(quickFind.connected(4, 3), True)

    def test_connect_transitive(self):
        quickFind = QuickFind(12)
        quickFind.union(1, 2)
        quickFind.union(2, 6)
        self.assertEqual(quickFind.connected(1, 6), True)

    def test_connect_2(self):
        quickFind = QuickFind(12)   
        quickFind.union(4, 3)
        quickFind.union(3, 8)
        quickFind.union(6, 5)
        quickFind.union(9, 4)
        quickFind.union(2, 1)
        self.assertEqual(quickFind.connected(0, 7), False)
        self.assertEqual(quickFind.connected(8, 9), True)
        quickFind.union(5, 0)
        quickFind.union(7, 2)
        quickFind.union(6, 1)
        quickFind.union(1, 0)
        self.assertEqual(quickFind.connected(0, 7), True)

class QuickFind:
    id = []

    def __init__ (self, n):
        self.id = [None]*n
        for i in range(n):
            self.id[i] = i

    def connected(self, p, q):
        print(self.id[p] == self.id[q])
        return self.id[p] == self.id[q]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]

        for i in range(len(self.id)):
            if (self.id[i] == pid):
                self.id[i] = qid


if __name__ == '__main__':
    unittest.main()