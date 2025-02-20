class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

def merge_sorted(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data < right.data:
        curr = left
        curr.next = merge_sorted(left.next, right)
    else:
        curr = right
        curr.next = merge_sorted(left, right.next)
    return curr

def merge_sort(head):
    if not head or not head.next:
        return head
    mid = find_mid(head)
    right_side = mid.next
    mid.next = None
    left_por = merge_sort(head)
    right_por = merge_sort(right_side)
    return merge_sorted(left_por, right_por)

def find_mid(head):
    if not head or not head.next:
        return head
    midd, mid_head = head, head.next
    while mid_head and mid_head.next:
        midd = midd.next
        mid_head = mid_head.next.next
    return midd




def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" , ")
        curr = curr.next

if __name__ == "__main__":
    head = Node(4)
    head.next = Node(2)
    head.next.next = Node(7)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(6)
    head.next.next.next.next.next = Node(3)
    head.next.next.next.next.next.next = Node(5)
    head = merge_sort(head)
    print_list(head)