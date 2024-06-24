# word = 'commitment'

# for letter in word:
#     if letter == 'm':
#         print(letter.capitalize())
#     else:
#         print(letter)

# word = 'commitment'
# favorite_letter = input('What is your favorite letter? ')

# for letter in word:
#     if letter == favorite_letter.lower():
#         print(letter.capitalize(), end='')
#     else:
#         print(letter, end='')

# word = 'commitment'
# favorite_letter = input('What is your favorite letter? ')

# for letter in word:
#     if letter == favorite_letter.lower():
#         print('_', end='')
#     else:
#         print(letter, end='')

quote = 'In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost.'

run_again = 'yes'

while run_again == 'yes':
    number = int(input('Please enter a number: '))

    for i, letter in enumerate(quote):
        if i % number == 0:
            print(letter.capitalize(), end='')
        else:
            print(letter.lower(), end='')
    
    print()

    run_again = input('Would you like to enter a different number? ').lower()

print('Goodbye.')