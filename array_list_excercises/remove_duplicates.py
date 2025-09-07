lst = [1, 1, 2, 2, 3, 4, 5]

def remove_duplicates(arr):
    clean = []
    for num in arr:
        if num in clean:
            continue    
        else:
            clean.append(num)
    return clean

print(remove_duplicates(lst))

def remove_duplicates2(arr):
    return list(set((arr)))

print(remove_duplicates2(lst))

def remove_duplicates3(arr):
    return list(dict.fromkeys(arr))

print(remove_duplicates3(lst))