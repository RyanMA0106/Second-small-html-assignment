# shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
# for item in shopping_list:
#     if item == 'spam':
#         print('i am ignoring {} it is gross'.format(item))
#         continue
#     print('buy ' + item)

# continue can be used to skip over a part of a loop that you don't want to run. above it is used to stop
# spam being printed. (bypasses for a particular part of code.) BE CAREFUL WITH YOUR INDENTING!!!
# meal = ['egg', 'bacon', 'spam', 'sausages']
#
# for item in meal:
#     if item == 'spam':
#         nasty_food_item = item
#         break
# else:
#     nasty_food_item = 'no_spam'
#     print('I will have a plate of that then please')
# else can be used in loops. it is however used for if the loop continues. so if break doesnt activate
# also else can follow the if so make sure it is indented right as you want it to follow the for not if

# if nasty_food_item != 'no_spam':
#     print('cant i have anything without spam in it')

# above can be done without break however it will continue te loop and if their are thousands of things in that list
# break would be way more efficient rather than continuing the list.
