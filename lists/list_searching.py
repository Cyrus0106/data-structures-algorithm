my_list = [1, 2, 3, 4, 5]
target = 4
if target in my_list:
    print("Target found in the list")
else:
    print("Target not found in the list")

# searching an element the worst case time complexity is O(n)
# searching an element the worst case space complexity is O(1)

# Linear Search
def linear_search(list,target):
    for i, value in enumerate(list):
        if value == target:
            return i
    return -1

# searching an array with linear search the worst case time complexity is O(n)
# searching an element the worst case space complexity is O(1)


my_list.sort()