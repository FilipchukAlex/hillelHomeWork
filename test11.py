matrix = [[2,3,5,2],[2,4,6,2],[-2,7,2,0]]
#matrix = [[5, 6, 4], [-2, 5, 3], [8, 7, -2]]
#matrix = [[3,2,1],[1,3,4]]

new_matrix = [list(i) for i in zip(*matrix)]

for i  in range(len(new_matrix)):
    if i in range(0, len(new_matrix), 2):
        new_matrix[i].sort(reverse=True)
    else:
        new_matrix[i].sort()

matrix = [list(i) for i in zip(*new_matrix)]
print(matrix)