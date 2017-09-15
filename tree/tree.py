
class Tree(object):
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        return self.root.in_order(print) 


    
class Node(object):
    def __init__(self, data, children=(None, None)):
        self.children = children
        self.data = data

    def __repr__(self):
        return str(self.data)

    def in_order(self, visit):
        if self.children[0]:
            self.children[0].in_order(visit)

        visit(self)

        if self.children[1]:
            self.children[1].in_order(visit)
    

left = Node(2)
right = Node(3)
n = Node(1, (left, right))
t = Tree(n)
n.in_order(print)
        
