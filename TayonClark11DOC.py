import heapq

def input_of_tree_values():
    n = int(input("Enter values of the tree:"))
    values = []
    print(f"Enter {n} integers:")
    for i in range(n):
        value = int(input())
        values.append(value)
    return values
def sort_in_order(arr):
    min_heap = []
    for val in arr:
        heapq.heappush(min_heap, val)
    sort_values = []
    while min_heap:
        sort_values.append(heapq.heappop(min_heap))
    return sort_values
def print_values(arr_sorted):
    print("The values sorted in decreasing order:")
    for val in reversed(arr_sorted):
        print(val, end=" ")
    print()

if __name__ == "__main__":
    Values_Of_Tree = input_of_tree_values()
    sortValues = sort_in_order(Values_Of_Tree)
    print_values(sortValues)
