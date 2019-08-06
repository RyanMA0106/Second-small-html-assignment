# string = '1234567890'

# for char in string:
#     print(char)
# an itterator returns individual items from the string and when their are none left it returns an error
# causing the end of the for loop

# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator)) # this will go through the list one at a time. it does what the for loop does
# print(next(my_iterator)) # more next iterations than the characters will cause an error an will crash the program
# a for loop uses this itteration for you so you do not have to do it manually

# for char in string:
#     print(char)
# for char in iter(string):  # this one is the same as the above because python uses iter for you implicitly so you
#     # don't need to
#     print(char)

# ITERATION MINI CHALLENGE
my_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
my_iter_list = iter(my_list)

for i in range (0, len(my_list)):
    print(next(my_iter_list))
# DON'T NEED TO USE THIS JUST USE FOR LOOPS NORMALLY THIS WAS TO HELP UNDERSTAND ITER FUNCTION ECT


