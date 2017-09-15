def get_data(node):
    return node.data

class Tree(object):
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        s = str(self.root.data)

    def inorder(self):
        staq = []
        inorder = []

        current = self.root
        while current or staq:

            while current:
                staq.append(current)
                current = current.children[0]

            current = staq.pop()
            inorder.append(current)
            current = current.children[1]

        return inorder

    def preorder(self):
        staq = []
        preorder = []

        current = self.root

        while current or staq:
            if current:
                preorder.append(current)
                staq.append(current.children[1])
                staq.append(current.children[0])
            current = staq.pop()

        return preorder


        


    
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
                

    def pre_order(self, visit):
        visit(self)
        
        if self.children[0]:
            self.children[0].pre_order(visit)

        if self.children[1]:
            self.children[1].pre_order(visit)

    def post_order(self, visit):
        if self.children[0]:
            self.children[0].pre_order(visit)

        if self.children[1]:
            self.children[1].pre_order(visit)

        visit(self)

l2 = Node(4)
left = Node(2, (l2, None))
right = Node(3)
n = Node(1, (left, right))
t = Tree(n)
# n.in_order(print)
# n.pre_order(print)
print(t.inorder())
print(t.preorder())
        
