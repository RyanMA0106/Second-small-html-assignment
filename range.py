# # my_list = list(range(10))
# # print(my_list)
# #
# # even = list(range(0, 10, 2))
# # odd = list(range(1, 10, 2))
# #
# # print(odd, even)
# # my_string = 'abcdefghijklmnopqrstuvwxyz'
# # print(my_string.index('e'))  # this returns the number that is at the characters position (counts from 0)
# # print(my_string[4])  # this returns the character that is 4 steps into the string (counts from 0) ie a == 0
#
# # can also be uses on range t find a part of a sequence ie..
# # example = range(0, 50, 10)
# # # print(example)
# # # print(example[4])
# # #
# small_decimals = range(0, 10)
# # # print(small_decimals.index(3))
# # # print(small_decimals[3])  # INDEX GIVES YOU THE PLACE IN THE SEQUENCE THE CHARACTER YOU GAVE IS AT ie 3
# # is place 4 in their
#
# # sevens = range(7, 100000, 7)
# # x = int(input('please enter a positive number less than one hundred thousand '))
# # if x in sevens:
# #     print('{} is divisible by seven'.format(x))
# # else:
# #     print('{} is not divisible by seven'.format(x))
#
# print(small_decimals)
#
# my_range = small_decimals[::2]  # gives the sequence in steps of two :: is used so you don't have to put in 0:10:2 or
# # 0, 10, 2 it is just used t leave it as original
# print(my_range)
# print(my_range.index(4))  # 4 in the new sequence is placed 2
# # range steps can also be in negatives ie -2 so it can step back from end number
#
# print(range(99, 0, -2) == range(0, 100)[::-2])
# # to get a negative step one of the tops must be done ie reverse the stert and finish 99, 0 instead of 0, 99
# # or 0, 100 [::-2} otherwise it will not work. so do not use 0, 99, -2 or it will return nothing
# # negative slices can be very useful for example
# backstring = 'egaugnal lufrewop yrev a si nohtyP'
# print(backstring[::-1])
#
# # can also reverse for loop like this
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

o = range(0, 100, 4)
print(o)
p = o[::5] # a slice of a range already in steps gives you the range in steps also in steps of the new step ie 5 meaning
# the old steps are multiplied by the new step so in this case 0, 100 in steps of 4 then done in steps of 5 is easier
# said as 0, 100 , 20 ie 4*5
print(p)
for i in p:
    print(i)
