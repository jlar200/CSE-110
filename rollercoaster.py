'''riders under 36in cannot ride, under 18 and 62in cannot ride alone
over 18 and 62in can ride alone, two riders can ride if one is over 18'''
    
# roller coastering
# jorja, jenna, josie, kimberly, sarah
# the best team

rider_1age = float(input('What is the age of the first rider? '))
rider_1height = float(input('What is the height of the first rider in inches? '))
multi_riders = input('Is there a second rider? YES or NO ' )


if multi_riders.lower() == 'yes':
    rider_2age = float(input('What is the age of the second rider? '))
    rider_2height = float(input("What is the height of the second rider in inches? "))

    # rule 1
    if rider_1height < 36 or rider_2height < 36:
        can_ride = False
    else:
        # rule 3
        if rider_1age >= 18 or rider_2age >= 18:
            can_ride = True
        else:
            can_ride = False

            # rule 4
            if rider_1age >= 12 and rider_1height >= 52 and rider_2age >= 12 and rider_2height >= 52:
                can_ride = True
            elif (rider_1age >= 16 and rider_2age >=14) or (rider_1age >= 14 and rider_2age >= 16):
                can_ride = True
            else: 
                can_ride = False

else: 
    # one rider
    if rider_1age >= 18 and rider_1height >= 62:
        can_ride = True
    else:
        can_ride = False

if can_ride:
    print("Welcome to the roller coaster of terror, be safe and have fun!!")
else:
    print("WOMP WOMP. You may not enter the ride!")