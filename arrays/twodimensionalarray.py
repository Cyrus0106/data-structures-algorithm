import numpy as np

twodimarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twodimarray)

def traverseTDArray(arr):
    for i in range(len(arr)):
        for y in range(len(arr)):
            print(arr[i][y])

def search_td_array(arr,target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == target:
                return i,j
    return -1


# searching an array with linear search the worst case time complexity is O(n^2)
# searching an element the worst case space complexity is O(1)
            
"""Deletion of an element from 2D array"""

new_array = np.delete(twodimarray, 0, axis=1)
print(new_array)
