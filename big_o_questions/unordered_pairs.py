def print_unordered_pairs(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])

# time complexity of O(n^2) because a loop is inside another for loop so O(n) * O(n) = O(n^2)


print_unordered_pairs([1, 2, 3, 4])