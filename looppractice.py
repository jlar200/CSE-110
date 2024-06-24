# loops continue to run until the desired condition is true.
# variables must be defined before being prompted for an input

#repeating until the entry fits the criteria
number = -1

while number < 0:
    number = int(input('Please enter a positive number: '))

print(f'The number is: {number}')

# instructor solution
# number = int(input('Please enter a positive number: '))
# while number < 0:
    # print('Sorry that is a negative number. Please try again.)
    # number = int(input('Please enter a positive number: '))
# print(f'The number is: {number}')'''


candy = ''

while candy != 'yes':
    candy = input('May I have a piece of candy? ')

print('Thank you!')
