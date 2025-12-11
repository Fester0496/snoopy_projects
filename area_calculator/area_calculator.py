from math import pi

# This program calculates the area of a shape: Square, Rectangle, Triangle or Circle

print('What kind of shape would you like to calculate the area for:')
print('1) Square. 2) Rectangle. 3) Triangle. 4) Circle.')
user_input = 0

while user_input != 5:

    user_input = int(input('Type the number for the shape: or 5) to Quit '))
    
    if user_input == 1:
        side = float(input('Ok type in the length of the side: '))
        area = side**2
        print(f'The area of the square is: {area}')
    elif user_input == 2:
        length = float(input('Type in the length of the rectangle: '))
        width = float(input('Type in the width of the rectangle: '))
        area = length * width
        print(f'The area of the rectangle is: {area}')
    elif user_input == 3:
        height = float(input('Type in the height of the Triangle: '))
        base = float(input('Type in the base of the triangle: '))
        area = (height*base) / 2
        print(f'The area of the triangle is: {area}')
    elif user_input == 4:
        radius = float(input('Type in the radius of the circle: '))
        area = pi * radius**2
        print(f'The area of the circle is: {area}')
    else: 
        print('Invalid input')