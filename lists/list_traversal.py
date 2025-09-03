# Accessing/Traversing list
shopping_list = ["apple", "banana", "cherry", "date", "elderberry"]
print(shopping_list[2])
print("apple" in shopping_list)

for item in shopping_list:
    print(item)

# Update/Insert - List
shopping_list[2] = "grape"
print(shopping_list)

# Delete/Remove - List
del shopping_list[3]
print(shopping_list)

# Append - List
shopping_list.append("kiwi")
print(shopping_list)

# Insert - List
shopping_list.insert(2, "mango")
print(shopping_list)

# Extend - List
fruits = ["orange", "peach"]
shopping_list.extend(fruits)
print(shopping_list)

# Slice - List
more_shopping = ["pear", "apricot"]
shopping_list[2:4] = more_shopping

# pop - List
shopping_list.pop(2)
print(shopping_list)

# delete element
del shopping_list[2]
print(shopping_list)