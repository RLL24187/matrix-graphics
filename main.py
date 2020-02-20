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


body = new_matrix(0, 0)
horns = new_matrix(0, 0)
eye = new_matrix(0, 0)
belly = new_matrix(0, 0)
spikes = new_matrix(0, 0)
claws = new_matrix(0, 0)
dragon = [body, horns, eye, belly, spikes, claws]

# head (outline)
add_edge(body, 5, 23, 0, 6, 24, 0)
add_edge(body, 6, 25, 0, 6, 26, 0)
add_edge(body, 8, 28, 0, 10, 27, 0)
add_edge(body, 7, 28, 0, 6, 28, 0)
add_edge(body, 6, 28, 0, 4, 27, 0)
add_edge(body, 4, 27, 0, 3, 25, 0)
add_edge(body, 3, 25, 0, 0, 23, 0)
add_edge(body, 0, 23, 0, 1, 21, 0)
add_edge(body, 1, 21, 0, 5, 22, 0)
add_edge(body, 5, 22, 0, 8, 23, 0)
add_edge(body, 8, 23, 0, 8, 24, 0)

# mouth
add_edge(body, 1, 21, 0, 5, 23, 0)

# nostril
add_edge(body, 1, 23, 0, 1, 22, 0)

# neck
add_edge(body, 8, 23, 0, 9, 22, 0)
add_edge(body, 10, 20, 0, 9, 22, 0)
add_edge(body, 14, 23, 0, 10, 27, 0)
add_edge(body, 14, 23, 0, 15, 20, 0)
add_edge(body, 14, 16, 0, 15, 20, 0)
    # beginning of belly area
add_edge(body, 8, 14, 0, 10, 20, 0)
add_edge(body, 8, 14, 0, 9, 10, 0)
add_edge(body, 9, 10, 0, 11, 8, 0)
    # later belly area
add_edge(body, 14, 7, 0, 16, 6, 0)
add_edge(body, 16, 6, 0, 20, 5, 0)
add_edge(body, 20, 5, 0, 26, 5, 0)
add_edge(body, 26, 5, 0, 28, 6, 0)
    # back
add_edge(body, 14, 16, 0, 18, 15, 0)

# first leg
add_edge(body, 9, 10, 0, 9, 9, 0)
add_edge(body, 9, 9, 0, 7, 5, 0)
add_edge(body, 7, 5, 0, 6, 4, 0)
add_edge(body, 10, 5, 0, 8, 4, 0)
add_edge(body, 10, 5, 0, 11, 7, 0)

# second leg
add_edge(body, 10, 14, 0, 10, 13, 0)
add_edge(body, 10, 13, 0, 11, 10, 0)
add_edge(body, 11, 10, 0, 11, 2, 0)
add_edge(body, 15, 12, 0, 15, 10, 0)
add_edge(body, 15, 10, 0, 14, 7, 0)
add_edge(body, 14, 7, 0, 14, 6, 0)
add_edge(body, 14, 6, 0, 13, 4, 0)
add_edge(body, 13, 4, 0, 13, 2, 0)

# third leg
add_edge(body, 27, 12, 0, 27, 10, 0)
add_edge(body, 27, 10, 0, 28, 6, 0)
add_edge(body, 28, 6, 0, 31, 4, 0)
add_edge(body, 31, 4, 0, 33, 3, 0)
add_edge(body, 33, 3, 0, 33, 2, 0)
add_edge(body, 35, 2, 0, 35, 4, 0)
add_edge(body, 35, 4, 0, 34, 6, 0)
add_edge(body, 34, 6, 0, 33, 7, 0)
add_edge(body, 33, 7, 0, 33, 10, 0)
add_edge(body, 33, 10, 0, 32, 12, 0)

# horns (and weird feathery thingies)
add_edge(horns, 8, 28, 0, 9, 29, 0)
add_edge(horns, 9, 29, 0, 7, 28, 0)
add_edge(horns, 6, 28, 0, 7, 29, 0)
add_edge(horns, 5, 28, 0, 7, 29, 0)
add_edge(horns, 5, 28, 0, 4, 27, 0)
add_edge(horns, 5, 25, 0, 7, 28, 0)
add_edge(horns, 8, 28, 0, 6, 26, 0)

# front feathery thingies
add_edge(horns, 15, 10, 0, 16, 9, 0)
add_edge(horns, 16, 10, 0, 16, 9, 0)
add_edge(horns, 16, 10, 0, 18, 11, 0)
add_edge(horns, 16, 11, 0, 18, 11, 0)
add_edge(horns, 16, 11, 0, 18, 13, 0)
add_edge(horns, 18, 13, 0, 15, 12, 0)

# back feathery thingies
add_edge(horns, 33, 10, 0, 34, 9, 0)
add_edge(horns, 34, 9, 0, 34, 10, 0)
add_edge(horns, 34, 10, 0, 35, 10, 0)
add_edge(horns, 35, 10, 0, 34, 11, 0)
add_edge(horns, 34, 11, 0, 36, 12, 0)
add_edge(horns, 33, 12, 0, 36, 12, 0)
add_edge(horns, 33, 12, 0, 34, 13, 0)
add_edge(horns, 32, 12, 0, 34, 13, 0)

# eye
add_edge(eye, 6, 26, 0, 5, 25, 0)
add_edge(eye, 7, 25, 0, 8, 28, 0)
add_edge(eye, 5, 25, 0, 7, 25, 0)
add_edge(eye, 6, 26, 0, 5, 25, 0)

# belly
add_edge(belly, 10, 20, 0, 9, 14, 0)
add_edge(belly, 9, 14, 0, 11, 10, 0)
add_edge(belly, 16, 9, 0, 21, 8, 0)
add_edge(belly, 21, 8, 0, 24, 8, 0)
add_edge(belly, 24, 8, 0, 27, 9, 0)

# white part of Yoshi's back
add_edge(belly, 18, 15, 0, 19, 13, 0)
add_edge(belly, 19, 13, 0, 23, 13, 0)
add_edge(belly, 23, 13, 0, 24, 15, 0)
add_edge(belly, 18, 15, 0, 19, 14, 0)
add_edge(belly, 19, 14, 0, 23, 14, 0)
add_edge(belly, 23, 14, 0, 24, 15, 0)

# red part of Yoshi's back
add_edge(horns, 18, 15, 0, 19, 16, 0)
add_edge(horns, 19, 16, 0, 23, 16, 0)
add_edge(horns, 23, 16, 0, 24, 15, 0)

# spikes
add_edge(spikes, 9, 29, 0, 6, 28, 0)
add_edge(spikes, 10, 27, 0, 11, 29, 0)
add_edge(spikes, 11, 29, 0, 9, 29, 0)
add_edge(spikes, 10, 27, 0, 11, 27, 0)
add_edge(spikes, 11, 27, 0, 13, 26, 0)
add_edge(spikes, 13, 26, 0, 12, 25, 0)
add_edge(spikes, 12, 25, 0, 13, 25, 0)
add_edge(spikes, 13, 25, 0, 15, 24, 0)
add_edge(spikes, 15, 24, 0, 14, 23, 0)
add_edge(spikes, 14, 23, 0, 15, 23, 0)
add_edge(spikes, 15, 23, 0, 17, 20, 0)
add_edge(spikes, 17, 20, 0, 15, 20, 0)
add_edge(spikes, 15, 20, 0, 16, 19, 0)
add_edge(spikes, 16, 19, 0, 16, 17, 0)
add_edge(spikes, 16, 17, 0, 14, 16, 0)


# feet
add_feet(body, 4, 2)
add_feet(body, 9, 0)
    # third foot
add_edge(body, 22, 4, 0, 24, 4, 0)
add_edge(body, 22, 3, 0, 24, 3, 0)
add_edge(body, 24, 3, 0, 25, 4, 0)
add_edge(body, 25, 4, 0, 26, 4, 0)
add_feet(body, 31, 0)

# claws
# third foot's claws
add_edge(claws, 21, 4, 0, 22, 5, 0)
add_edge(claws, 21, 4, 0, 22, 4, 0)
add_edge(claws, 22, 3, 0, 22, 5, 0)
add_edge(claws, 21, 3, 0, 22, 3, 0)
add_edge(claws, 21, 3, 0, 22, 4, 0)
add_edge(claws, 27, 4, 0, 26, 5, 0)
add_edge(claws, 26, 5, 0, 26, 4, 0)
add_edge(claws, 26, 4, 0, 27, 4, 0)
# first foot
add_claws(claws, 3, 2)
# second foot
add_claws(claws, 8, 0)
# last foot
add_claws(claws, 30, 0)

i = 0
for body_part in dragon:
    scalar_mult(body_part, 11)
    if i < 1:
        color = [0, 255, 0]
    elif (i < 2):
        color = [255, 0, 0]
    else:
        color = [255, 255, 255]
    i += 1
    draw_lines(body_part, screen, color)

display(screen)
