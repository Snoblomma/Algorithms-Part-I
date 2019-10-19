import unittest

class TestQueueLinkedList(unittest.TestCase):
    def test(self):
        queueLinkedList = QueueLinkedList()
        s = 'to be or not to - be - - that - - - is'
        d = s.split(' ')
        for i in d:
            if i == '-':
                queueLinkedList.dequeue()
            else:
                queueLinkedList.enqueue(i)

        self.assertEqual(queueLinkedList.output(), 'that')

class Node(object):
    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class QueueLinkedList(object):
    first: Node = None
    last: Node = None

    def __init__(self, head=None):
        self.first = head

    def isEmpty(self):
        return self.first == None

    def enqueue(self, item):
        oldlast = self.last
        self.last = Node()
        self.last.item = item
        self.last.next_node = None
        if (self.isEmpty()):
            self.first = self.last
        else:
            oldlast.next_node = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next_node
        if (self.isEmpty()):
            self.last = None
        return item

    def output(self):
        res = []
        current = self.first
        while current.next_node != None:
            res.append(current.item)
            current = current.next_node
        return ' '.join(res)

if __name__ == "__main__":
    unittest.main()