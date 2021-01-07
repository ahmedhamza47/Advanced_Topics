# normally a lambda is similar to a function
from functools import reduce

# adder = lambda x: x + 10
#
# print(adder(5))
#
# multiply = lambda x,y,z: x*y*z # creates a function that returns the mul of 3 arguments
#
# print(multiply(2,3,4))
#
# # sorting elements using lambda
elements = [5,4,7,2,8,]
# sorted_element = sorted(elements,key= lambda x: x < x+1)
# print(sorted_element)


# mapping elements
map_elements = map(lambda x: x + 2,elements)
print(list(map_elements))

# filter elements
f = filter(lambda x:x % 2 == 0,elements)
print(list(f))
# better method is
filter_elements = [x for x in elements if x % 2 == 0]
print(filter_elements)

# reduce function
red = reduce(lambda x,y: x * y,elements)  # returns a single value
print(red)

