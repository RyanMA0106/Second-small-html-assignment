# ip_address = input('please enter an ip address ')
# print(ip_address.count('.'))
# # above is used to count a certain thing in a list or variable ect
# parrot_list = ['not pinin\' ', 'no more ', 'a stiff ', 'bereft of life ']
# for state in parrot_list:
#     print('this parrot is' + state)
# bellow is used to change list
# parrot_list.append('A Norwegian Blue')
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# can sort lists better so instead of just tacking odds onto the list you can make them numerical
# numbers.sort()
# print(numbers)
# numbers.sort changes the list cannot be used to make new variable ie print(numbers.sort)
# if you wanted a new variable it would be done like print(sorted(numbers))

# lists can be added to each other to make a new list

# list_1 = []
# list_2 = list()
# # both of the above create an empty list
# # list 2 is using a constructor and this can have other uses such as making a list with individual letters of a string
# # ie
# print(list('the strings are equal'))
#
# even = [2, 4, 6, 8]
# another_even = even
# another_even.sort(reverse=True)
# print(even)
# print(another_even is even)  # should show true as they use same list
# # 2 variables can refer to the same list ie above meaning sorting the 2nd variable affects the first as they both call
# # upon the same list
# # you can change this however by making them the same bt use different lists using th elist constructor
# # ie
# even = [2, 4, 6, 8]
# another_even = list(even)
# another_even.sort(reverse=True)
# print(even)  # therefore the origional list is not changed as their ar 2 separate lists
# print(another_even is even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
number = (even, odd)  # this will return 2 lists on the same line
print(number)

for numbers_set in number:
    print(numbers_set)

    for value in numbers_set:
        print(value)
# 1st for loop goes through just the lists in the loop but the second for loop
# goes through the values in those individual lists
