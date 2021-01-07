import random

# num = random.random()  # prints  a random floating number
# print(num)
#
# num1 = random.randint(1,10)  # gives a random integer between 1 & 10
# print(num1)

num2 = random.randrange(1,10,2)  # never picks 10 we can also add steps in it
print(num2)

num3 = random.normalvariate(0,1)  # used in statistics i.e. normal distribution
print(num3)

alp = list('ABCDEFGHIJ')
print(random.choice(alp))
print(random.sample(alp,2))  # prints 2 elements from given list
print(random.choices(alp,k=3))  # can pick same element multiple times

random.shuffle(alp)
print(alp)

import secrets  # secrets is used for passwords authentications specially

print(secrets.randbelow(10))  # returns a random no. form 0-10
print(secrets.randbits(4))    # returns a no. with 4 bits, highest possible in 4 bits is 1111 i.e. 15

print(secrets.choice(alp))

import numpy as np

arr = np.random.randint(1,10,3) # returns an array of 3 elements ranging from 1-10
arr2 = np.random.randint(1,10,(3,3)) # returns 3*3 array
print(arr)
print(arr2)




