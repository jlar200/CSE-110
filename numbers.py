# working with numbers assignment. convert to a string using str()
# convert to a number using int() for whole numbers or float() for numbers that may require a decimal

age=input('How old are you?')
older_age= int(age)+1
birthday_age= str(older_age)
print('On your next birthday you will be '+birthday_age +'.')
print(' ')

egg_cartons=input('How many egg cartons do you have?')
number_eggs= int(egg_cartons)*12
egg_estimation= str(number_eggs)
print('You have ' +egg_estimation +' eggs.')
print(' ')

cookie_count=input('How many cookies are there?')
people_count=input('How many people are there?')
cookie_per= int(cookie_count)/int(people_count)
print('Each person can have '+str(cookie_per) +' cookies.')
# string and integer conversions can be placed in the code as it works, though only when not converting it back.