#matrix = [[2,3,5,2],[2,4,6,2],[-2,7,2,0]]
matrix = [[5, 6, 4], [-2, 5, 3], [8, 7, -2]]
#matrix = [[3,2,1],[1,3,4]]
def coord_s_points(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max(matrix[i][j] for i in range(len(matrix))):
                result.append([i, j])
    return result


print(coord_s_points(matrix))
