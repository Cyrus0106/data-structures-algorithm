from array import *

arr = array('i', [1, 2, 3, 4])
arr2 = array('d', [1.1, 2.2, 3.3, 4.4])

# print(arr2)

def traverse_array(arr):
    for i in arr:
        print(i)

traverse_array(arr)

# the time complexity of traversing an array is O(n)
# the space complexity of traversing an array is O(1)