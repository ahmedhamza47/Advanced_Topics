# multiplication
x = 5 * 2
print(x)

# power
y = 2 ** 3
print(y)

# for making a list or tuple
lst = [0] * 10
tup = '5' * 10
print(lst)
print(tup)

# for function arguments
def func(a,b,*c,**d):
    print(a,b)
    for arguments in c:
        print(arguments)
    for key in d:
        print(key,d[key])

func(1,2,3,4,5,six =6,seven = 7,eight = 8)

# using list
my_list = [1,2,3,4,5,6]
begin,mid,*last = my_list
print(begin,mid,last)

# merging two lists,tuples,dictionary
list_a = [1,2,'a']
list_b = [3,4,'b']

print(*list_a,*list_b)

dict_1 = {'name':'hamza','roll':6,'city':'ktm'}
dict_2 = {'section':'A','class':12}
merged_dict = {**dict_1,**dict_2}
# or we can do following
print({**dict_1,**dict_2})
