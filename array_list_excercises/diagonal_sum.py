matrix = [[1, 2, 3],
            [4, 5, 6],
             [7, 8, 9]]

print(matrix[1][1])

def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

print(diagonal_sum([[1, 2, 3],
            [4, 5, 6],
             [7, 8, 9]]))