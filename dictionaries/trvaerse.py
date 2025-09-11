dict = {'name': 'Shaivonte', 'age': 20, 'gender': 'male'}

def traverse_dict(dict):
    for key in dict:
        print(key, dict[key])

traverse_dict(dict)

# time complexity of traversing a dictionary is O(n)
# space complexity of traversing a dictionary is O(1)