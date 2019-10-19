import unittest

class TestEvaluate(unittest.TestCase):
    def test_evaluate(self):
        expression = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'
        evaluate = Evaluate(expression)
        self.assertEqual(evaluate.result, 101)

class StackResizingArray(object):
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

class Evaluate(object):
    result = 0

    def __init__(self, expression):
        ops = StackResizingArray()
        vals = StackResizingArray()
        splitted = expression.split(' ')
        for s in splitted:
            if s == "(":
                pass 
            elif s == "+":
                ops.push(s)
            elif s == "*":
                ops.push(s)
            elif s == ")":
                op = ops.pop()
                if op == "+":
                    vals.push(int(vals.pop()) + int(vals.pop()))
                elif op == "*":
                    vals.push(int(vals.pop()) * int(vals.pop()))
            else:
                vals.push(s)
                
        self.result = vals.pop()


if __name__ == "__main__":
    unittest.main()