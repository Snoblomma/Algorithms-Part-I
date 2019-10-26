import unittest

class TestPriorityHeap(unittest.TestCase):
    def test(self):
        a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
        heap = Heap()
        self.assertEqual(heap.sort(a), ['A', 'E', 'E', 'L', 'M', 'O', 'P', 'R', 'S', 'T', 'X'])


class Heap(object):

    def sort(self, a):
        N = len(a) - 1
        leastParent = N / 2
        for i in range (int(leastParent), -1, -1):
            self.sink(a, i, N)
        
        for i in range (N, 0, -1):
            if a[0] > a[i]:
                a[0], a[i] = a[i], a[0]
                self.sink(a, 0, i - 1)

        return a

    def sink(self, a, k=int, N=int):
        largest = 2 * k + 1
        while largest <= N:
            if (largest < N) and (a[largest] < a[largest + 1]):
                largest += 1
        
            if a[largest] > a[k]:
                a[largest], a[k] = a[k], a[largest]
                k = largest
                largest = 2 * k + 1
            else:
                return
                

if __name__ == "__main__":
    unittest.main()