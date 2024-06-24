print('You are hiking a new trail and take a wrong turn. Do you use your phone to CALL for help? or do you go BACK the way you came?')
option_1 = input('Which do you choose: CALL or BACK? ')

if option_1.upper() == 'CALL':
    print("You can't seem to get a good enough signal to make a call.")
    option_2 = input('Do you WALK farther to continue looking for a signal or do you try to SHOUT for help? (WALK or SHOUT) ')
    if option_2.upper() == 'WALK':
         print('As you walk staring at your phone you trip on a root. Looking up you see a purple glow coming from somewhere up ahead.')
         option_3 = input('Do you move TOWARD or AWAY from the glow? (TOWARD or AWAY) ')
         if option_3.upper() == 'TOWARD':
             print('As you move forward, you hear voices. The closer you get the lighter your head feels. You blackout as you hear someone call your name.')
         elif option_3.upper() == 'AWAY':
             print('You hear a voice whisper your name, getting further and further away. Somehow you find your way back to the path and your car.')
         else:
             print('Invalid option. Please try again.')
    elif option_2.upper() == 'SHOUT':
         print('You hear your voice echo back to you. As silence once again fills the air, you could swear you hear a voice whispering your name, moving further and further away.')
         option_4 = input('Do you IGNORE the whisper or do you try to FOLLOW it? (IGNORE or FOLLOW) ')
         if option_4.upper() == 'IGNORE':
             print('As you continue to walk you do your best to tune out the voice. Walking away from it you find yourself back on the trail.')
         elif option_4.upper() == 'FOLLOW':
             print('The voice leads you directly to a purple portal. As you reach out to touch it you suddenly find yourself waking up in your bed.')
         else:
            print('Invalid option. Please try again.')
    else:
         print('Invalid option. Please try again.')

elif option_1.upper() == 'BACK':
     print('As you start to make your way back things start looking less and less familiar.')
     option_5 = input('Do you CONTINUE walking or do you STOP and try to get your bearings? (CONTINUE or STOP) ')
     if option_5.upper() == 'CONTINUE':
         print('A purple glow comes from up ahead. It looks to be some sort of portal.')
         option_6 = input('Do you go THROUGH the portal or do you TEST it with a stick? (THROUGH or TEST) ')
         if option_6.upper() == 'THROUGH':
             print('As you come out the other side of the portal, you find yourself in the setting of your favorite book.')
         elif option_6.upper() == 'TEST':
             print('At first the stick goes through the portal. Then suddenly the portal rejects it with a burst of energy that throws you backward.')
         else:
             print('Invalid option. Please try again.')
     elif option_5.upper() == 'STOP':
         print('As you look around you see a purple glow. You hear it seem to whisper your name.')
         option_7 = input('Do you WALK toward it, ANSWER it, or RUN away? (WALK, ANSWER or RUN) ')
         if option_7.upper() == 'WALK':
             print('As you move toward it you feel it start to pull you in. Before you can resist the warm glow sucks you in and you blackout.')
         elif option_7.upper() == 'ANSWER':
             print("You call out to the voice that you hear but it only continues to call your name. As you back away it slowly fades, but the shiver down your spine doesn't.")
         elif option_7.upper() == 'RUN':
             print('The whisper quickly fades as you run. Somehow you find your way back to your car. You swear never to come back to this trail.')
         else:
             print('Invalid option. Please try again.')

else:
    print('Invalid option. Please try again.')
