# print('Hello!')
# name = input('What is your name?')
# age = int(input('How old are you, {0}?'.format(name)))
# if age >= 18:
#     print('You are old enough to vote')
# else:
#     print('You are not old enough to vote, please come back in {0} years'.format(18 - age))
#
# print('please guess a number between 1 and 10: ')
# guess = int(input())
# if guess != 5:
#     if guess <5:
#         print('please guess higher')
#     else: # guess needs to be greater han 5
#         print('please guess lower')
#
#     guess = int(input())
#     if guess == 5:
#         print('Well done!, you guessed it')
#     else:
#         print('sorry you have not guessed correctly')
# else:
#     print('wow! you got it first time ')

# age = int(input('How old are you? '))
# the brackets bellow do not change anything but make the code easier to read
# if (age >= 16) and (age <=65):
# you can change the code above to code bellow
# if 16 <= age <= 65:
# can also be done like bellow
# if 15 < age < 66:
#   print('Have a good day at work!')
# if (age < 16) or (age > 65):
#    print('Enjoy your free time!')
# else:
#   print('Have a good day at work!')
# if x will be true if x has a value however if it does not then it will be false this can be used for
# input('please enter some text')
# if x:
#     print('thank you for entering something')
# else:
#     print('you did not enter any text')
# not is used to reverse the value ie..
# print(not False)
# print(not True)
# the not function can be used as such
# age = int(input('please enter your age '))
# if not (age < 16):
#     print('you are old enough to vote')
#     print('please vote in this upcoming election')
# else:
#     print('you are not old enough to vote, please come back in {0} years'.format(18 - age))
# main reason for this function is to check if a condition is not met
# in is another function and can be used to check if something is in something else ie..
# parrot = 'Norwegian Blue'
# letter = input('enter a character ')
# if letter in parrot:
#     print('give me an {}, bob'.format(letter))
# else:
#     print('I don\'t need that letter')
print('Hello and welcome to Holiday central, lets check if you are eligible ')
name = input('please start off by telling us your name ')
print('welcome {}'.format(name))
age = int(input('now please tell us your age {} '.format(name)))
if 18 <= age < 31:
    print('Great news you are able to get the deal on our holiday!')
else:
    print('sorry, unfortunately you are not able to get the deal on our holiday')
    print('please check some of our other offers')







