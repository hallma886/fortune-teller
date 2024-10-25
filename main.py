# Matthew Hall
# October 23, 2024
#Fortune Teller

import random
import sys
import time

fortunes = ["You are a winner", "A secret admirer will soon send you a sign of affection!", "The one you love is much closer than you think!", "Good things will happen to you by the end of the day today!", "Fame and fortune will be yours if you take the time to learn Python!", "I'm just a computer program, and have no magical powers!"]

magic_colors = ['blue', 'red', 'green', 'yellow']

user_name = input('please enter your first name:\n')

print(f"Welcome to my Python Fotune Teller program {user_name}!")
print()
fortune_question = input("Do you want me to tell you your fortune? [y/n]:\n")
time.sleep(2)
if fortune_question == 'y' or 'yes':
    time.sleep(1)
    magic_color_Q = input("Okay! To get your fortune, please input a magic color: [blue/red/green/yellow]\n")
    time.sleep(1)
    print('Getting your fortune')
    time.sleep(2)
    print()
    #print(f'Here is you fortune {user_name}!')
    if magic_color_Q in magic_colors:
        print(f'Here is you fortune {user_name}!')
        print(fortunes[random.randint(0, len(fortunes) - 1)])
    else: 
        print(f"Please choose a magic color of either 'blue', 'red', 'green', or 'yellow'.")
        time.sleep(1)
        print(f"Once you have input a magic color, I will reveal your fortune!")
else:
    print(f"Thank you for playing my Fortune Teller game today, {user_name}!")
    print('Goodbye')
    sys.exit()