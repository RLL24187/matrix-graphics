from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)

m0 = new_matrix(0, 0)
add_point(matrix, 1, 2)

print_matrix(matrix)


draw_lines( matrix, screen, color )
display(screen)
