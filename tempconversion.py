# converts fahrenheit to celsius and rounds to the tenths
fahren_temp = float(input('What is the temperature in Fahrenheit?'))
celsius_temp = (fahren_temp - 32) * (5 / 9)

print(f'The temperature in Celsius is {celsius_temp:.1f} degrees.')
