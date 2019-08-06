# # tuples are done with commas for example 'a', 'b', 'c' people may say they are done in brackets however that
# # is not the case unless it is used to get rid of confusion. for example print ('a', 'b', 'c') will just print a
# string
# # however to make it more clear it is best to just use brackets in cases of tuples
# # so in this case a 2nd set of brackets are needed to make this a tuple.
# # when returned through running tuples are shown in round brackets.
# # tuples cannot be amended after being created.#
#
# welcome = 'Welcome to my nightmare', 'Alice Cooper', 1975  # this is a tuple
# bad = ('Bad company', 'Bad company', 1974)  # this is also a tuple this way is probably best as it is clearer
# budgie = ('Night flight', 'Budgie', 1981)
# imelda = ('More mayhem', 'Emilda May', 2011)
# metallica = 'Ride the Lightning', 'Metallica', 1984
#
# print(metallica)
# print(metallica[0])  # prints the first part of the tuple ie ride the lighning
# print(metallica[1])
# print(metallica[2])

# Although you cannot change tuples in most ways you can splice to change up errors ie
# metallica[0] = 'master of puppets' will not work
# imelda = (imelda[0], 'Imelda May', imelda[2])  # but this on the other hand will work
# tuples are immutable and lists are mutable, this means that abov cannot change the tuple it just creates a new one.
# lists are intended to hold items of the same type but tuples are intended to hold different this means that tuples
# are very useful

# the tuples above can be useful in this way

# title, artist, year = imelda
# all of the variables are assigned a part from the tuple imelda, so title is imelda[0] artist is imelda[1]
# and year is imelda[2] THIS IS CALLED UNPACKING A TUPLE

# tuples can also contain tuples for example adding the name of each track to this list
imelda = ('More mayhem', 'Emilda May', 2011, (
    (1, 'pulling the rug'), (2, 'psycho'), (3, 'mayhem'), (4, 'kentish town waltz')))
# each of the tracks here are individual tuples in a tuple and the brackets are used to separate them so the track
# numbers are assigned properly
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)

# you can however unpack this even further by making them all individual tuples on their own ie
imelda = ('More mayhem', 'Emilda May', 2011, (1, 'pulling the rug'), (2, 'psycho'), (3, 'mayhem'), (4, 'kentish town waltz'))

title, artist, year, tracks1, tracks2, tracks3, tracks4 = imelda
print(title)
print(artist)
print(year)
print(tracks1)
print(tracks2)
print(tracks3)
print(tracks4)
# this looks cleaner however you need to know the amount of tracks before hand where as in the one above
# the tracks amount does not matter as they are all in a one tuple
