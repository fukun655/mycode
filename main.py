def rotate(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()


# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(rotate(matrix))

# The 'matrix' will be rotated 90 degrees clockwise in-place
# and will become:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]
