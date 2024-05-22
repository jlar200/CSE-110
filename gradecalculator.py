# calculate a letter grade
grade_percent = float(input('What is your grade percentage? '))

if grade_percent >= 90:
    print('You have an A.')
elif grade_percent >= 80:
    print('You have a B.')
elif grade_percent >= 70:
    print('You have a C.')
elif grade_percent >= 60:
    print('You have a D.')
else:
    print('You have an F.')
print()

if grade_percent >= 70:
    print('Congratulations on passing the class!')
else:
    print('You did not pass the class. Try again next semester.')
print()

#streamlining the grade calculation by turning the print statements into a variable
if grade_percent >= 90:
    letter = ('A')
elif grade_percent >= 80:
    letter = ('B')
elif grade_percent >= 70:
    letter = ('C')
elif grade_percent >= 60:
    letter = ('D')
else:
    letter = ('F')
print(f'You have a(n) {letter}.')
print()

# denoting a plus or minus grade
remainder = grade_percent % 10
if remainder >= 7:
    indicator = ('+')
elif remainder < 3:
    indicator = ('-')
else:
    indicator = ('')

# limiting A and F to no + or -
if grade_percent >= 93:
    indicator = ('')

if letter == ('F'):
    indicator = ('')

print(f'You got a(n) {indicator}{letter}.')
print()
