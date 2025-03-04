from queue import Queue

def inputOfArray():
    arr = list(map(int, input("Enter numbers for the array:").split()))
    return arr

def reverseArray(arr):
    q = Queue()

    for item in arr:
        q.put(item)

    reversedArr = []
    while not q.empty():
        reversedArr.insert(0, q.get())

    return reversedArr

def main():
    arr = inputOfArray()
    reversedArr = reverseArray(arr)
    print(reversedArr)

if __name__ == "__main__":
    main()

