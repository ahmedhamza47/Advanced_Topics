# itertools: product, permutation, combination
from itertools import product,permutations,combinations,combinations_with_replacement,accumulate,groupby
from itertools import count,repeat,cycle
import operator
a = [1,2]
b = [3,4]
# prod = product(a,b) # cartesian product
# print(list(prod))

c = [1,2,3]
# perm = permutations(c) # arrangement of the elements
# print(list(perm))
# perm2 = permutations(c,2) # specifying the elements in 1 permutation
# print(list(perm2))


# com = combinations(c,2)
# print(list(com))
# com1 = combinations_with_replacement(c,2)
# print(list(com1))


d = [1,2,6,4,5]
print(d)
acc = accumulate(d)  # add the next digit with previous one
print(list(acc))

acc1 = accumulate(d,func=operator.mul)
print(list(acc1))

acc2 = accumulate(d,func=max)
print(list(acc2))


group = [{'name':'hamza','age':'47'},{'name':'ahmed','age':'22'},{'name':'soni','age':'22'},{'name':'ramesh','age':'47'}]
# groups the given lists according to the requirements
obj = groupby(group,key=lambda x:x['age'])
for key,value in obj:
    print(key,list(value))

for i in repeat(1,5):
    print(i)