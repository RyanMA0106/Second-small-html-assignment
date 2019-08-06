# range bellow will always miss the end number hence nt show 20 if you want up to 20 end at 21
# i in for loops is acceptable as it is taken short for index
# for i in range(1,20):
#     print('i is now {}'.format(i))
# len is a function that stands for length it returns the length of a string
# number = '9,223,372,036,854,775,807'
# for i in range(0, len(number)):
#     print(number[i])
# number{i} gives you the part of the variable number that i is at
# if you needed go through some data and ignore the commas or the full stops used you can do it like so
# number = '9,223,372,036,854,775,807'
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         print(number[i],end='')
# end='' is used to stop everything being put on separate lines
# number = '9,223,372,036,854,775,807'
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print('The number is {}'.format(newNumber))
# above would be how to get the number into a variable int IT IS VERY IMPORTANT NOT TO TAB NEW NUMBER, this is as
# if you tab it then every digit will create a newNumber variable and with massive numbers this can be very bad for pc

# you can clean up the first way of doing it by using char which is character
# number = '9,223,372,036,854,775,807'
# cleanedNumber = ''
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
# newNumber = int(cleanedNumber)
# print('the number is {}'.format(newNumber))
#
# for state in ['not pinin', 'no more', 'a stiff', 'bereft of life']:
#     print('this parrot is {}'.format(state))
# # or ('this parrot is'+ state)
# range can also be used with a step like so
# for i in range(0, 101, 5):
#     print('i is {}'.format(i))
# this can be used to make childrens multiplication table like so
# for i in range(1, 13):
#     for j in range(1, 13):
#         print('{0} times {1} is {2}'.format(i, j, i*j))
#     print('==================')
# for last print watch indent level as where it is it does it per block but if it was indented 1 more it would
# do it per calculation if you anted it as a table you could change
# print('{0} times {1} is {2}'.format(i, j, i*j), end='\t') but you would need last print to be blank to look better


