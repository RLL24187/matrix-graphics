"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    string = ""
    for r in range (len(matrix[0])):
        for c in matrix:
            string += str(c[r]) + " "
        string += "\n"
    print(string)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for c in range (len(matrix)):
        for r in range (len(matrix[c])):
            if (c != r):
                matrix[c][r] = float(0)
            else:
                matrix[c][r] = float(1)

def scalar_mult (matrix, scalar):
    for c in range (len(matrix)):
        for r in range (len(matrix[c])):
            matrix[c][r] *= scalar
def shift_updown (matrix, shift_amt):
    for c in range(len(matrix)):
        matrix[c][1] += shift_amt
def shift_rightleft (matrix, shift_amt):
    for c in range(len(matrix)):
        matrix[c][0] += shift_amt
#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    # number of cols in m1 = number of rows in m2
    # print(len(m1))
    # print(len(m2[0]))
    if (len(m1) != len(m2[0])):
        return
    # product matrix will have dimensions (rows m1) x (cols m2)
    for r in range (len(m2)):
        m2[r] = mult_help(m1, m2[r])


def mult_help(m1, col):
    # multiply elements of rows in m1 by elements of each col in m2 and total them
    temp = []
    for i in range (len(m1)):
        total = 0
        for r in range (len(m1[i])):
            # print(str(m1[r][i]) + " * " + str(col[r]))
            total += m1[r][i] * col[r]
        temp.append(total)
    return temp # returns the new row


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( float(0) )
    return m
