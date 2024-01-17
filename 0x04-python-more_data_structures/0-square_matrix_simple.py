#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    New_Matrix = matrix.copy()
    for i in range(len(matrix)):
        New_Matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return (New_Matrix)
