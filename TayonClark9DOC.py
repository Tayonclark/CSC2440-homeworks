class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binarysearchtree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.recursive(self.root, data)

    def recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.recursive(node.right, data)

    def calcsumof5(self, node):
        if node is None:
            return 0
        total = 0
        if node.data % 5 == 0:
            total += node.data
        total += self.calcsumof5(node.left)
        total += self.calcsumof5(node.right)
        return total

    def traversal(self, node):
        if node:
            self.traversal(node.left)
            print(node.data, end="")
            self.traversal(node.right)

BST = Binarysearchtree()

userInput = int(input("Enter the nodes of the Binary Search Tree: "))
print(f"Enter {userInput} values for the Binary Search Tree")
for _ in range(userInput):
    UInput = int(input())
    BST.insert(UInput)

print("\nInOrder Traversal")
BST.traversal(BST.root)
print("\n")

CalSum5 = BST.calcsumof5(BST.root)
print(f"The sum of those divisible by 5 is {CalSum5}")


