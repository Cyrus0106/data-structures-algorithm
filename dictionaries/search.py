dict = {'name': 'Shaivonte', 'age': 20, 'gender': 'male'}

def search_dict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return None


# delete an element from dictionary
del dict['age']
print(dict)
# time complexity of deleting an element from a dictionary is O(1)
# space complexity of deleting an element from a dictionary is O(1)

removed_element = dict.pop('gender')
print(dict)
print(removed_element)
# time complexity of deleting an element from a dictionary is O(1)
# space complexity of deleting an element from a dictionary is O(1)

dict.clear()
print(dict)
