import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

def linear(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Target found at index {i}"
    return "Target not found"

def binary_search(arr,target):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"Target found at index {mid}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return "Target not found"






def max_product(arr):
    max = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] * arr[j] > max and i != j:
                max = arr[i] * arr[j]
    return max                

print(max_product([1, 7, 3, 4, 9, 5]))

def max_product2(arr):
    num1, num2 = 0,0 
    for num in arr:
        if num > num1:
            num2 = num1
            num1 = num
        elif num > num2:
            num2 = num
    return num1 * num2

print(max_product2([1, 7, 3, 4, 9, 5]))