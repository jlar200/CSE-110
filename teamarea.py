# area of a square
side= float(input('What is the length of the side of a square? '))
area= side**2
print('The area of the square is: ' +str(area))
# print(f'The area of the square is: {area}')
print()

# area of a rectangle
length= float(input('What is the length of the rectangle?'))
width= float(input('What is the width of the rectangle?'))
area_rec= length*width
print('The area of the rectangle is: ' +str(area_rec))
print()

# area of a circle
radius= float(input('What is the radius of the circle?'))
area_circ= 3.14*(radius**2)
print('The area of the circle is: ' +str(area_circ))
print()

# pi stretch assignment
import math
area_circ_2= (math.pi)* (radius**2)
print(f'The area of a circle is: {area_circ_2}')
print()

