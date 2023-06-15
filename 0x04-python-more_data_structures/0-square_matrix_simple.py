#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for col in matrix:
        ans = list(map(lambda x: x**2, col))
        my_matrix.append(ans)
    return my_matrix
