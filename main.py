from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

add_point(matrix, 1, 2)
print_matrix(matrix)

m0 = new_matrix(2, 2)
ident(m0)
print_matrix(m0)

m1 = new_matrix(4, 3)
add_point(m1, 3, 3)
print_matrix(m1)
ident(m1)
print_matrix(m1)


draw_lines( matrix, screen, color )
display(screen)
