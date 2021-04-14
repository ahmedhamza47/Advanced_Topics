# def print_name(name): <- name here is a parameter
#   print(name)

# calling a function
# print_name('Hamza') <- Hamza is an argument
# ---------------------------------------------------------------------------------
def func(a,*b):
    print(a)
    # print(list(i for i in b))
    print(list(i for i in b))
func(1,2,3,4)
# --------------------------------------------------------------------------------------
# positional argument
def numbers(a,b):
    print(a,b)

numbers(1,2)

# -------------------------------------------------------------------------------------
# keyword arguments
def num(a,b,c):
    print(a,b,c)
num(a = 1,b = 2,c = 3)
num(c=4,b=5,a=1)
# ------------------------------------------------------------------------------------
def printing(a,b,*c,**d): # we can pass any no. of arguments in c and **d is a key argument parameter
    print(a,b)
    for i in c:
        print(i)
    for key in d:
        print(key,d[key])

printing(1,2,3,4,5,six = 6,seven = 7)
# -----------------------------------------------------------------------
def function(first,*mid,last): # we need to use key word argument for last to specify the value
    print(first)
    for i in mid:
        print(i)
    print(last)

function(1,2,3,4,last = 5)

# -----------------------------------------------------------------------------------------
# using lists,tuples and dictionary in function

def func(name,roll,section):
    print(name,roll,section)

my_list = ['hamza',5,'A']
func(*my_list)

my_tuple = ('soni',8,'A')
func(*my_tuple)

my_dict = {'name': 'Sabin','roll': 38,'section': 'A'}
func(**my_dict)

# ----------------------------------------------------------------------------
