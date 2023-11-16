from PrintBinaryTree import display

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def PrintNode(self):
        print(self.val)

# class BinaryTree:
#     def __init__(self):
    #def insert(self, data):
        #using breadth-first inserts to keep it balanced


test = Node(10)
display(test)
