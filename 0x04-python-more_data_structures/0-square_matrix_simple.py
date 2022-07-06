#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    temp = [[x[i]**2 for i in range(len(matrix))] for x in matrix]
    return temp
print(square_matrix_simple([[4,5,6],[1,3,8],[10,11,12]]))
