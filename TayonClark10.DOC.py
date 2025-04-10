class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert_value(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_value(root.left, data)
    else:
        root.right = insert_value(root.right, data)
    return root

def traversal(root):
    if root:
        traversal(root.left)
        print(root.data, end=" ")
        traversal(root.right)

def sum_of_3_largest(root, k):
    def ri(node):
        nonlocal count, total, k_Value
        if node and count < k:
            ri(node.right)
            if count < k:
                total += node.data
                count += 1
                k_Value = node.data
            ri(node.left)

    def sum_k(node):
        if node:
            if node.data >= k_Value:
                return node.data + sum_k(node.left) + sum_k(node.right)
            else:
                return sum_k(node.right)
        return 0
    count = 0
    total = 0
    k_Value = None
    ri(root)
    return sum_k(root)

if __name__ == "__main__":
    root = None
    print("Enter BST vaules:")
    values = list(map(int, input().split()))
    for val in values:
        root = insert_value(root, val)

    print("\n")
    traversal(root)

    k = int(input("\n\nEnter k's value"))
    result = sum_of_3_largest(root, k)
    print(f"Sum of elements >= {k}: {result}")




