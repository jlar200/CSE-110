import random

print('Welcome to the word guessing game!')

list_of_word = ['basket','blanket', 'computer', 'house', 'shoe', 'hoodie']

word = random.choice(list_of_word)
counter = 0
revealed = '_' * len(word)

while revealed != word:
    print(f"Your hint is: {revealed}")
    guess = input('What is your guess? ').lower()
    counter += 1
    new_revealed = ''

    if len(guess) != len(word):
        print("Please enter a guess that is exactly " + str(len(word)) + " letters long.")
        continue


    for i in range(len(word)):
        if guess[i] == word[i]:
            new_revealed += word[i].upper()
        elif guess[i] in word:
            new_revealed += guess[i]
        else:
            new_revealed += '_'

    revealed = new_revealed
    

    if revealed.lower() == word:
        print('Congratulations! You guessed it!')
        print(f'It took you {counter} guesses.')
        break
    else:
        print('Your guess was not correct')