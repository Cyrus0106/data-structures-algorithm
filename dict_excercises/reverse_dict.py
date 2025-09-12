
def reverse_dict(my_dict):
    # TODO
    result = {}
    for i in my_dict:
        result[my_dict[i]] = i
    return result

print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))


def reverse_dict2(my_dict):
    return {v: k for k, v in my_dict.items()}