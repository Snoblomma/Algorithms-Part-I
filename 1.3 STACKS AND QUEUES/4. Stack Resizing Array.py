import unittest

class TestStackOfStrings(unittest.TestCase):
    def test_stack(self):
        s = 'to be or not to - be - - that - - - is'
        d = s.split(' ')
        stackOfStrings = ResizingArrayStackOfStrings()
        for i in d:
            if i == '-':
                stackOfStrings.pop()
            else:
                stackOfStrings.push(i)
        self.assertEqual(stackOfStrings.getString(), 'to is')

class ResizingArrayStackOfStrings(object):
    N = 0
    s = []

    def __init__(self):
        self.s = ['']
    
    def isEmpty(self):
        return self.N == 0

    def push(self, item):
        if self.N == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.N] = item
        self.N += 1
    
    def pop(self):
        self.N -= 1
        item = self.s[self.N]
        self.s[self.N] = None
        return item
    
    def getString(self):
        res = []
        for i in self.s:
            if i != None:
                res.append(i)
        return ' '.join(res)

    def resize(self, capacity):
        copy = [None]*capacity
        for i in range(self.N):
            copy[i] = self.s[i]
        self.s = copy

if __name__ == "__main__":
    unittest.main()