#
# CS 415 - Mini Project 4
# Connor Shyan
# UIC, Fall 2022
# Referencing geeksforgeeks.org extensively for function definitions
#

import numpy as np
import cv2
import math


#
# Function that returns new coordinates after rotating (counterclockwise by default)
#
def rotate(angle, point_x, point_y, around_x, around_y):
    new_point_x, new_point_y = point_x - around_x, point_y - around_y
    theta = np.radians(angle)
    cos, sin = np.cos(theta), np.sin(theta)
    transformation_matrix = ([cos, sin],
                             [-sin, cos])
    original_coordinates = ([new_point_x, new_point_y])
    res = np.dot(transformation_matrix, original_coordinates)
    return int(res[0] + around_x), int(res[1] + around_y)


#
# P1. Applying Geometric Transformations to Pixel Coordinates
#

# Creating All White Image of 500x500 resolution
image = np.full((500, 500, 3), 255, dtype=np.uint8)

# Drawing red circle at point a = (100, 40)
image = cv2.circle(image, (100, 40), 10, (0, 0, 255), -1)

# Rotate point a around origin in clockwise direction by 60 degrees to get point b
bx, by = rotate(-60, 100, 40, 0, 0)

# Drawing green circle at point b
image = cv2.circle(image, (bx, by), 10, (0, 255, 0), -1)

# Drawing black circle at point c = (100, 100)
image = cv2.circle(image, (100, 100), 10, (0, 0, 0), -1)

# Rotate point a around point c in clockwise direction by 60 degrees to get point d
dx, dy = rotate(-60, 100, 40, 100, 100)

# Drawing blue circle at point d
image = cv2.circle(image, (dx, dy), 10, (255, 0, 0), -1)

# Showing final image with all circles
# cv2.imshow("Final P1 Image", image)
# cv2.waitKey()
# cv2.destroyAllWindows()


#
# P2. Self-Study of cv2.warpAffine() method
#

# Getting lena.png image and reading shape
lena = cv2.imread("lena.png")
rows, cols, ch = lena.shape

# Moving image to the right by 100 pixels and to the bottom by 200 pixels
move_matrix = np.float32([[1, 0, 100],
                          [0, 1, 200]])
moved_lena = cv2.warpAffine(lena, move_matrix, (cols, rows))
cv2.imwrite("p2_lena_moved.png", moved_lena)

# Flipping image horizontally with respect to the image center
flip_matrix = np.float32(([-1, 0, cols],
                          [0, 1, 0]))
flipped_lena = cv2.warpAffine(lena, flip_matrix, (cols, rows))
cv2.imwrite("p2_lena_flipped.png", flipped_lena)

# Rotate the image around the origin in the clockwise direction by 45 degrees
theta = np.radians(-45)
cos, sin = np.cos(theta), np.sin(theta)
rotate_matrix_1 = np.float32(([cos, sin, 0],
                              [-sin, cos, 0]))
rotated_lena_1 = cv2.warpAffine(lena, rotate_matrix_1, (cols, rows))
cv2.imwrite("p2_lena_rotated1.png", rotated_lena_1)

# Rotate the image around the image center in the clockwise direction by 45 degrees
rotate_matrix_2 = cv2.getRotationMatrix2D((cols/2, rows/2), -45, 1)
rotated_lena_2 = cv2.warpAffine(lena, rotate_matrix_2, (cols, rows))
cv2.imwrite("p2_lena_rotated2.png", rotated_lena_2)
