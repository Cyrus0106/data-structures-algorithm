def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])

# time complexity of O(n^2) because a loop is inside another for loop so O(n) * O(n) = O(n^2)
