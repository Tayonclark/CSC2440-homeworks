def insert_New_Number(arr, n, x, pos):

    for i in range(n - 1, pos -1, -1):
        arr[i + 1] = arr[i]
    arr[pos] = x

if __name__ == "__main__":
    arr = [3, 6, 4, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    n = 4
    x = 7
    pos = 0

    insert_New_Number(arr, n, x, pos)
    n += 1
    for i in range(0, n):
        print(arr[i], end=" ")


