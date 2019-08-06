fruit = {'orange': 'a sweet, orange, citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour yellow citrus fruit',
         'grape': 'a small sweet fruit growing in bunches',
         'lime': 'a sour, green citrus fruit'}

print(fruit['lemon'])

bike = {'make': 'Honda', 'model': '250 dream', 'colour': 'red', 'engine_size': 250}
# you can add to a dictionary by doing bellow
# square brackets for adding one in as in dictionary square brackets are always used for the 'key'
fruit['pear'] = 'an odd shaped apple'
print(fruit)
# if you add another entry with the same name it replaces the old one rather than add a new with same name
# ie
fruit['lime'] = 'great with tequila'
print(fruit)
# you can also delete entries ie
# del fruit['lemon']
print(fruit)
# make sure you use del with care as if not specified it will delete the entire dictionary
# ie
# del fruit
# you can also empty he dictionary ready to edit it in some other way with
# fruit.clear()
# you can cause an error if you try to acess a key that isnt in the dictionary ie
# print(fruit['tomato'])
# you can use code like bellow to let people access the dictionary
while True:
    dict_key = input('enter a fruit you want a description for ')
    if dict_key == 'quit':
        break
    description = fruit.get(dict_key)
    print(description)
# above also ensures that anything typed not in dictionary returns 'nothing' rather than an error
# you could also go a step further like this to add a description to that
while True:
    dict_key = input('enter a fruit you want a description for ')
    if dict_key == 'quit':
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        print(description)
    else:
        print('sorry we have no description for that')
