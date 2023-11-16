from PrintBinaryTree import display

class BSTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def PrintNode(self):
        print(self.val)

    def insert(self, data):
        if self:
            if data <= self.val:
                print(data, '<=', self.val)
                if self.left is None:
                    print('insert left')
                    self.left = BSTNode(data)
                else:
                    self.left.insert(data)
                
            if data > self.val:
                print(data, '>', self.val)
                if self.right is None:
                    print('insert right')
                    self.right = BSTNode(data)
                else:
                    self.right.insert(data)
            

test = BSTNode(10)

test.insert(3)
test.insert(12)
test.insert(5)
test.insert(1)
test.insert(0)


print('left of 10' , test.left)

display(test)