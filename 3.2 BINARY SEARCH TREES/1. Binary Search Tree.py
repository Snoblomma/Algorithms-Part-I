class Node(object):

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1

class BST(object):

    def __init__(self):
        self.root = Node()

    def putRoot(self, key, val):
        self.root = self.put(self.root, key, val)
    
    def put(self, x, key, val):
        if x == None:
            return Node(key, val)

        if (key < x.key):
            x.left = self.put(x.left, key, val)
        elif (key > x.key):
            x.right = self.put(x.right, key, val)
        elif (key == x.key):
            x.val = val
        
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x

    def get(self, key):
        x = self.root
        while x != None:
            if (key < x.key):
                x = x.left
            elif (key > x.key):
                x = x.right
            elif (key == x.key):
                return x.val
        return None

    def floorRoot(self, key):
        x = self.floor(self.root, key)
        if x == None:
            return None
        return x.key

    def floor(self, x, key):
        if x == None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return self.floor(x.left, key)

        t = self.floor(x.right, key)
        if t != None:
            return t
        else:
            return x

    def sizeRoot(self):
        return self.size(self.root)

    def size(self, x):
        if x == None:
            return 0
        return x.count

    def rankRoot(self, key):
        return self.rank(key, self.root)

    def rank(self, key, x):
        if x == None:
            return 0
        if key < x.key:
            return self.rank(key, x.left)
        elif key > x.key:
            return 1 + self.size(x.left) + self.rank(key, x.right)
        elif key == x.key:
            return self.size(x.left)
        
    def deleteMinRoot(self):
        self.root = self.deleteMin(self.root)

    def deleteMin(self, x):
        if x.left == None:
            return x.right
        x.left = self.deleteMin(x.left)
        x.count = 1 + self.size(x.left) + self.size(x.right)
        return x
    
    def min(self, x):
        if x.left == None:
            return x
        else:
            x = x.left
            return self.min(x)
        
    def deleteRoot(self, key):
        self.root = self.delete(self.root, key)

    def delete(self, x, key):
        if x == None:
            return None

        if key < x.key:
            x.left = self.delete(x.left, key)
        elif key > x.key:
            x.right = self.delete(x.right, key)
        else:
            if x.right == None:
                return x.left
            if x.left == None:
                return x.right

            t = x
            x = self.min(t.right)
            x.right = self.deleteMin(t.right)
            x.left = t.left

        x.count = self.size(x.left) + self.size(x.right) + 1
        return x