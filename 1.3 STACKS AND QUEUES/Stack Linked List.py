import unittest

class TestStackOfStrings(unittest.TestCase):
    def test_stack(self):
        s = 'to be or not to - be - - that - - - is'
        stackOfStrings = StackOfStrings()
        self.assertEqual(stackOfStrings.stack(s), 'is to')

class Node:

    def __init__ (self, item, next):
        self.item = item
        self.next = next


class LinkedStackOfStrings:

    first = None
    #  = Node(None, None)
    # = None

    def __init__ (self):
        self.first = Node(None, None)

    def isEmpty(self):
        return self.first == None
    
    def push(self, item: str):
        oldfirst = self.first
        self.first = Node(None, None)
        self.first.item = item
        self.first.next = oldfirst

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        return item

if __name__ == "__main__":
    linkedStackOfStrings = LinkedStackOfStrings()
    s = 'to be or not to - be - - that - - - is'
    d = s.split(' ')
    for i in d:
        if i == '-':
            linkedStackOfStrings.pop()
        else:
            linkedStackOfStrings.push(i)
    print(linkedStackOfStrings)
    # unittest.main()