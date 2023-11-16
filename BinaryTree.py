from PrintBinaryTree import display

class BTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def PrintNode(self):
        print(self.val)

    def insert(self, data):
        #using breadth-first inserts to keep it balanced
        q = [self]

        while len(q) > 0:
            curr = q.pop(0)
            if curr.left == None:
                curr.left = BTNode(data)
                return self
            if curr.right == None:
                curr.right = BTNode(data)
                return self
            
            q.append(curr.left)
            q.append(curr.right)



test = BTNode(10)

test.insert(3)
test.insert(5)
test.insert(1)
test.insert(0)

display(test)