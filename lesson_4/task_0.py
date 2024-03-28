# Напишите функцию для транспонирования матрицы

import itertools

matrix = [[3, 3, 3], [4, 4, 4], [5, 5, 5]]

def transposition_matrix(matrix) -> list[list[int]]:
    lines = len(matrix)
    columns = len(matrix[0])
    transposed = [[0 for _ in range(lines)] for _ in range(columns)]
    for i, j in itertools.product(range(lines), range(columns)):
        transposed[j][i] = matrix[i][j]
    return transposed


result = transposition_matrix(matrix)

for row in result:
    print(row)