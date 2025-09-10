def foo(array):
    sum = 0 
    product = 1
    for i in array:
        sum += i
    for i in array:
        product *= i
    print(f"Sum: {sum}, Product: {product}")

# Time complexity of O(n) the for loops are both linear and since they arent imbedded this would be O(2n) which is O(n)