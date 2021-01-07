# generators are much more  memory efficient and are used when u have a large no. of code
# they are powerful advanced python technique
import sys
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
# # for i in gen:
# #     print(i)
# # or we can do
# # val = next(gen)  # prints 1
# # print(val)
# # val = next(gen)  # prints 2
# # print(val)
# # val = next(gen)  # prints 3
# # print(val)
#
# print(sorted(gen))

# fibonacci series using generators

def fibonacci(limit):
    a,b = 0,1
    while a <= limit:
        yield a
        a,b = b,a+b

fib = fibonacci(10)
print((i for i in fib))

# generator comprehension similar to list comprehension but generator uses much smaller size than a list
generator = (i for i in range(10000000) if i % 2 == 0)
lst = [i for i in range(10000000) if i % 2 == 0]

print(sys.getsizeof(generator))
print(sys.getsizeof(lst))