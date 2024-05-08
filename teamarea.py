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

# area and volume of square and circle stretch assignment
single_length= float(input('What is the length?'))
square_area= single_length*2
circle_area= math.pi * (single_length**2)
print(f'The area of a square with that length side is: {square_area}')
print(f'The area of a circle with that length radius is: {circle_area}')
cube_vol= single_length**3
sphere_vol= (4/3)*math.pi*(single_length**3)
print(f'The volume of a cube of that length is: {cube_vol}')
print(f'The volume of a sphere of that radius is: {sphere_vol}')
print()

# areas in centimeters and meters
centi_side= float(input('What is the length of the side of a square in centimeters? '))
centi_area= centi_side**2
meter_area= centi_area/10000
print(f'The area of the square in centimeters is: {centi_area}')
print(f'The area of the square in meters is: {meter_area}')
print()

centi_length= float(input('What is the length of the rectangle in centimeters?'))
centi_width= float(input('What is the width of the rectangle?'))
centi_rec= centi_length*centi_width
meter_rec= centi_rec/10000
print(f'The area of the rectangle in centimeters is: {centi_rec}')
print(f'The area of the rectangle in meters is: {meter_rec}')
print()

centi_radius= float(input('What is the radius of the circle in centimeters?'))
centi_circ= 3.14*(centi_radius**2)
meter_circ= centi_circ/10000
print(f'The area of the circle in centimeters is: {centi_circ}')
print(f'The area of the circle in meters is: {meter_circ}')
print()
