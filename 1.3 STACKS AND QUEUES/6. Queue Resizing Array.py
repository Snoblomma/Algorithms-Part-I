import unittest

class TestQueueResizingArray(unittest.TestCase):
    def test_queue(self):
        s = 'to be or not to - be - - that - - - is'
        d = s.split(' ')
        queueResizingArray = QueueResizingArray(len(d))
        for i in d:
            if i == '-':
                queueResizingArray.dequeue()
            else:
                queueResizingArray.enqueue(i)
        self.assertEqual(queueResizingArray.getString(), 'to that is')

class QueueResizingArray(object):
    head = 0
    tail = 1
    s = []

    def __init__(self, capacity):
        self.s = ['']
    
    def isEmpty(self):
        return self.head == 0

    def enqueue(self, item):
        if self.tail == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.tail] = item
        self.tail += 1
    
    def dequeue(self):
        self.head -= 1
        item = self.s[self.head]
        self.s[self.head] = None
        return item
    
    def getString(self):
        res = []
        for i in self.s:
            if i != None and i != '':
                res.append(i)
        return ' '.join(res)

    def resize(self, capacity):
        copy = [None]*capacity
        for i in range(self.tail):
            copy[i] = self.s[i]
        self.s = copy

if __name__ == "__main__":
    unittest.main()