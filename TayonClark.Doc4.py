from inspect import stack


def Array():
    MyArray = list(map(int, input("Enter the Numbers for the array: ").split()))
    return MyArray

def ReverseArray(MyArray):
    stack = []
    for element in MyArray:
        stack.append(element)
    reversedArray = []
    while stack:
        reversedArray.append(stack.pop())
    return reversedArray

MyArray = Array()
reversedArray = ReverseArray(MyArray)
print(reversedArray)