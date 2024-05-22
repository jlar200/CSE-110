# this program is to build conditional statements

first_number = input('What is the first number? ')
second_number = input('What is the second number? ')

if first_number > second_number:
    print('The first number is greater.')
else:
    print('The first number is not greater.')

if first_number == second_number:
    print('The numbers are equal.')
else:
    print('The numbers are not equal.')

if first_number < second_number:
    print('The second number is greater.')
else:
    print('The second number is not greater.')
print()

# This function matches the input in order to respond.

fav_animal = input('What is your favorite animal? ')

if fav_animal.lower() == 'dog':
    print("That's my favorite too!")
else:
    print('That one is not my favorite.')
