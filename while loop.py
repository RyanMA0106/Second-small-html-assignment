# for i in range(10):
#     print('i is now {}'.format(i))
# # while loops can be used to achieve same ie..
# i = 0
# while i < 10:
#     print('i is now {}'.format(i))
#     i += 1
# example of while loop use in game
# available_exits = ['east', 'north east', 'south']
# chosen_exit = ''
# while chosen_exit not in available_exits:
#     chosen_exit = input('chose a direction to travel')
#     if chosen_exit == 'quit':
#         print('Game over!')
#         break
# else:
#     print('thank god we made it out of their!')

# RANDOM GENERATION
import random

highest = 1000
answer = random.randint(1, highest)
# bellow is good but only get 2 guesses
# print('please give a number between 1 and {}: '.format(highest))
# guess = int(input())
# if guess != answer:
#     if guess < answer:
#         print('plese guess higher')
#     else:
#         print('please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print('well done you got it!')
#     else:
#         print('sorry you have not guessed correctly')
# else:
#     print('you got it first time')
guess = 0
# ^^ used to initalize while loop but cant be inside valid range
print('please give a number between 1 and {}: '.format(highest))
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print('plese guess higher or quit with 0')
    elif guess > answer:
        print('please guess lower or quit with 0')
    else:
        print('well done you got it')



