
def max_value_key(my_dict):
    # TODO
    highest_key = "a"
    vall = 0
    for key, value in my_dict.items():
        if value > vall:
            vall = value
            highest_key = key
    return highest_key

print(max_value_key({'a': 5, 'b': 9, 'c': 2}))


def max_value_key1(my_dict):
    return max(my_dict, key=my_dict.get)
