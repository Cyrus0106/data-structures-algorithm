
def merge_dicts(dict1, dict2):
    # TODO
    merged = dict1.copy()
    for i in merged:
        if i in dict2:
            merged[i] = merged[i] + dict2[i]
    for i in dict2:
        if i not in merged:
            merged[i] = dict2[i]
    return merged

print(merge_dicts({'a': 1, 'b': 2, 'c': 3},{'b': 3, 'c': 4, 'd': 5}))