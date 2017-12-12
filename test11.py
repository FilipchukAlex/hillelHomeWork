matrix = [[2,3,5,2],[2,4,6,2],[-2,7,2,0]]
#matrix = [[5, 6, 4], [-2, 5, 3], [8, 7, -2]]
#matrix = [[3,2,1],[1,3,4]]


def matrix_transpose(matrix):
    new_matrix = [[0  for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]
    return new_matrix


matrix_transposed = matrix_transpose(matrix)

for i  in range(len(matrix_transposed)):
    if i in range(0, len(matrix_transposed), 2):
        matrix_transposed[i].sort(reverse=True)
    else:
        matrix_transposed[i].sort()

print(matrix)
print(matrix_transpose(matrix_transposed))
