new_tuple = ('a', 'b', 'c', 'd', 'e')
# print(new_tuple)
# print(type(new_tuple))
# print(new_tuple[0])

# time complexity of creating a tuple is O(1) because it is contastant
# space complexity of creating a tuple is O(n) because it depends on the amount of elements


# print(new_tuple[1])
# print(new_tuple[1:4])

# time complexity of accessing an element in a tuple is O(1)
# space complexity of accessing an element in a tuple is O(1)

# for i in new_tuple:
#     print(i)

# time complexity of traversing a tuple is O(n)
# space complexity of traversing a tuple is O(1)

print('a' in new_tuple)
print(new_tuple.index('a'))

def search_tuple(tuple,target):
    for i in range(len(tuple)):
        if tuple[i] == target:
            return i
    return -1


print(search_tuple(new_tuple,'a'))