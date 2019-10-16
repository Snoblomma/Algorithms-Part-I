import unittest

class TestStackOfStrings(unittest.TestCase):
    def test_stack(self):
        s = 'to be or not to - be - - that - - - is'
        d = s.split(' ')
        stackOfStrings = FixedCapacityStackOfStrings(len(d))
        for i in d:
            if i == '-':
                stackOfStrings.pop()
            else:
                stackOfStrings.push(i)
        self.assertEqual(stackOfStrings.getString(), 'to is')

class FixedCapacityStackOfStrings(object):
    N = 0
    s = []

    def __init__(self, capacity):
        self.s = [None]*capacity
    
    def isEmpty(self):
        return self.N == 0

    def push(self, item):
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

if __name__ == "__main__":
    unittest.main()