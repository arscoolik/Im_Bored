def findsmall(arr, size): #if we have all numbers between 1 and size, then it will print size+1, otherwise the first number that is not between 1 and size
    for i in arr:
        if 0 <= abs(i) - 1 < size:
            arr[abs(i) - 1] = min(-arr[abs(i) - 1], arr[abs(i) - 1])#numbers that have been found turnn negative
    for i in range(size):
        if arr[i] > 0:
            return i + 1
    return size + 1


arr = [1, 3, 6, 1324, 5, 2, 2]
print(findsmall(arr, len(arr)))

