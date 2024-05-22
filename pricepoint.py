# calculates the total cost of a meal based on the prices of children and adult meals

kid_meal=float(input("What is the price of a child's meal?"))
adult_meal=float(input("What is the price of an adult's meal?"))
number_kids=int(input('How many children are there?'))
number_adults=int(input('How many adults are there?'))
tax_rate=float(input('What is the sales tax rate?'))
print()
kid_total= kid_meal*number_kids
adult_total= adult_meal*number_adults
subtotal= kid_total + adult_total
sales_tax= tax_rate/100
tax_amount=subtotal*sales_tax
complete_total= subtotal+tax_amount
print(f'Subtotal: ${subtotal}')
print(f'Sales Tax: ${tax_amount}')
print(f'Total: ${complete_total}')
print()

payment=float(input('What is the payment amount?'))
change= payment-complete_total
print(f'Your change is: ${change:.2f}')
print()

print('Thank you for coming in today!')
print('Enjoy your meal!')
