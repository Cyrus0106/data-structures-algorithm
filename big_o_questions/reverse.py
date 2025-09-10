def reverse(arr):
    for i in range(0,int(len(arr)/2)):
        other = len(arr) - 1 - i
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    print(arr)

# time complexity is O(n)