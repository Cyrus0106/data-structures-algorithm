def check_same_frequency(list1, list2):
    # TODO
    if len(list1) != len(list2):
        return False
    for i in list1:
        if list1.count(i) != list2.count(i):
            return False
    return True



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))

def check_same_frequency2(list1, list2):
    freq_dict1 = {}
    freq_dict2 = {}
    for i in list1:
        freq_dict1[i] = freq_dict1.get(i, 0) + 1
    for i in list2:
        freq_dict2[i] = freq_dict2.get(i, 0) + 1
    
    return freq_dict1 == freq_dict2