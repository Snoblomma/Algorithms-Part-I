import unittest

class TestStackOfStrings(unittest.TestCase):
    def test_stack(self):
        s = 'to be or not to - be - - that - - - is'
        stackOfStrings = StackOfStrings()
        self.assertEqual(stackOfStrings.stack(s), 'is to')


class StackOfStrings:
    def stack(self, s: str):
        stack = list()
        d = s.split(' ')
        for i in d:
            if i == '-':
                stack.remove(stack[0])
            else:
                stack.insert(0, i)
        return ' '.join(stack)

if __name__ == "__main__":
    unittest.main()