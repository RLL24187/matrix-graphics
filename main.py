from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

m2 = new_matrix(0, 0)

print("Testing add_edge (which implements add_point): Adding (1, 2, 3), (4, 5, 6)  m2 = ")
add_edge(m2, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Testing ident: m1 (before) =")
m1 = new_matrix(4, 3)
add_point(m1, 3, 3)
print_matrix(m1)

print("m1 (after ident) =")
ident(m1)
print_matrix(m1)


print("Testing matrix_mult: m1 * m2")
m1 = new_matrix(0, 0)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 7, 8, 9, 10, 11, 12)
print("m1 = ")
print_matrix(m1)
print("m2 = ")
print_matrix(m2)

matrix_mult(m1, m2)
print("m1 * m2 = ")
print_matrix(m2)
# add_point(matrix, 1, 2)
# print_matrix(matrix)
#
# m0 = new_matrix(2, 2)
# ident(m0)
# print_matrix(m0)
#

dragon = new_matrix(0, 0)

# head
add_edge(dragon, 5, 25, 0, 7, 28, 0)
add_edge(dragon, 6, 26, 0, 5, 25, 0)
add_edge(dragon, 5, 25, 0, 7, 25, 0)
add_edge(dragon, 6, 26, 0, 5, 25, 0)
add_edge(dragon, 8, 28, 0, 6, 26, 0)
add_edge(dragon, 8, 28, 0, 9, 29, 0)
add_edge(dragon, 8, 28, 0, 10, 27, 0)
add_edge(dragon, 10, 27, 0, 11, 29, 0)
add_edge(dragon, 11, 29, 0, 9, 29, 0)
add_edge(dragon, 9, 29, 0, 7, 28, 0)
add_edge(dragon, 7, 28, 0, 6, 28, 0)
add_edge(dragon, 6, 28, 0, 7, 29, 0)
add_edge(dragon, 7, 29, 0, 4, 27, 0)
add_edge(dragon, 5, 28, 0, 4, 27, 0)
add_edge(dragon, 4, 27, 0, 3, 25, 0)
add_edge(dragon, 3, 25, 0, 0, 23, 0)
add_edge(dragon, 0, 23, 0, 1, 21, 0)
add_edge(dragon, 1, 21, 0, 22, 5, 0)
add_edge(dragon, 22, 5, 0, 8, 23, 0)

# nostril
add_edge(dragon, 1, 23, 0, 1, 22, 0)

draw_lines( matrix, screen, color )
display(screen)
