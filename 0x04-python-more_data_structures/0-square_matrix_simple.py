#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for col in matrix:
        ans = list(map(lambda x: x**2, col))
        new_matrix.append(ans)
    return new_matrix
