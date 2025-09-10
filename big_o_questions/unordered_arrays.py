def print_unordered_pairs(arr1,arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] < arr2[j]:
                print(arr1[i],arr2[j])


# time complexity of O(n) because each loop is traversing different arrays and they are both linear