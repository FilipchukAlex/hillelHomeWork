#matrix = [[2,3,5,2],[2,4,6,2],[-2,7,2,0]]
matrix = [[5, 6, 4], [-2, 5, 3], [8, 7, -2]]
#matrix = [[3,2,1],[1,3,4]]

def matrix_transpon(matrix):
    for i in range(len(matrix)):
      for j in range(i,len(matrix[i])):
          matrix[j][i], matrix [i][j] = matrix[i][j], matrix[j][i]
    return matrix


matrix_transpon(matrix)
for i  in range(len(matrix)):
    if i in range(0, len(matrix), 2):
        matrix[i].sort(reverse=True)
    else:
        matrix[i].sort()

print(matrix_transpon(matrix))
