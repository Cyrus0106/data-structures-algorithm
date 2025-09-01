import array

arr = array.array('i', [1, 2, 3, 4])

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr, 10))

# searching an array with linear search the worst case time complexity is O(n)
# searching an element the worst case space complexity is O(1)