def rotate_matrix(matrix):
    return [list(reversed(row)) for row in zip(*matrix)]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_matrix(matrix)
print(rotated_matrix)