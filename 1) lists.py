my_list = [1,2,3,4,5,6,7,8,9]

print(my_list[-5:-1]) # prints last 3 elements excluding the last one
print(my_list[1:9])
print(my_list[1:9:2])
print(my_list[::])

my_list.insert(3,22) # insert an element at specific position
print(my_list)

print(my_list[::-1]) # reverse the list

# to make a copy of one list to  another
new_list = my_list.copy()
new_list.append(100)
print(new_list)

# list comprehension
b = [i*i for i in my_list]
print(b)
