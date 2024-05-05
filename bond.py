first_name=input('What is your first name?')
last_name=input('What is your last name?')
# output= {last_name}, {first_name}; {last_name}
# print('Your name is ' output '.')
# the above two lines did not work
output= f'Your name is {last_name}, {first_name} {last_name}.'
print(output)

'''this allows for a comment that stretches across multiple lines
Anything between the quotations will not appear when the code is run'''
