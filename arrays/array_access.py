from array import array

arr = array('i', [1, 2, 3, 4])

def access_element(array,index):
    if index > len(array) - 1:
        return "Index out of range"
    else:
        return array[index]

print(access_element(arr,3))

# accessing an element the worst case time complexity is O(1)
# accessing an element the worst case space complexity is O(1)