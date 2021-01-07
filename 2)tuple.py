my_tuple = ('hamza', 'ahmed', 2)

print(my_tuple)

# note elements cant be inserted or deleted into the tuples i.e my_tuple.append() not possible

new_tuple = tuple(['undertaker', 2, 100]) # turning a list into a tuple
print(new_tuple)

print(new_tuple.count(2)) # counts no. of same  elements in the tuple

print(my_tuple.index('hamza')) # finds the index of element in tuple


name, cast, roll = my_tuple
print(name, cast, roll)

i1, *i2 = my_tuple
print(i1)
print(i2) # i2 gets the remaining elements of the tuple and converts them to a list

