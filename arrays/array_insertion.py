import array

arr = array.array('i', [1, 2, 3, 4])
print(arr)
arr.insert(2, 6)
print(arr)

# inserting an element the worst case time complexity is O(n)
# inserting an element the worst case space complexity is O(1) because only one place is needed
