# This one is to display an id badge with varying identifiers
first_name=input('What is your first name?')
last_name=input('What is your last name?')
email_address=input('What is your email address?')
phone_number=input('What is your phone number?')
job_title=input('What is your job title?')
id_number=input('What is your ID number?')
print('')
output= f'{last_name.upper()},{first_name}'
print(output)
print(job_title.title())
print('ID: '+id_number)
print(' ')
print(email_address.lower())
print(phone_number)