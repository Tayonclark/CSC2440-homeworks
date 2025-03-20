class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self, root):
        self.root = Node(root)
    def InsertValue(self, node, value, position):
        if node is None:
            return

        if node.value == position:
            if node.left is None:
                node.left = Node(value)
            elif node.right is None:
                node.right = Node(value)
            return
        self.InsertValue(node.left, value, position)
        self.InsertValue(node.right, value, position)


    def NewOrder(self, node):
        if node:
            self.NewOrder(node.left)
            self.NewOrder(node.right)
            print(node.value, end=" ")

Bt = Binary_Tree(5)
Bt.root.left = Node(3)
Bt.root.right = Node(2)
Bt.root.left.left = Node(4)

Bt.InsertValue(Bt.root, 6, 3)
Bt.NewOrder(Bt.root)
