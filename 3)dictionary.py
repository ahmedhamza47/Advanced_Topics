
my_dict = {'name':'hamza','age':'27', 'roll': '47','mother':{'father':'naseem'}}
print(my_dict)

new_dict = dict(name = 'hamza',age = '47')
print(new_dict)

my_dict['email'] = 'hamza@yahoo.com'
print(my_dict)

del my_dict['email']
print(my_dict)

if 'age' in my_dict:
    print(my_dict['age'])

for keys in my_dict.keys(): # for printing keys of the dictionary
    print(keys)
# also you can do
for keys,value in my_dict.items():
    print(keys,value)

dict_copy = my_dict.copy()
dict_copy['lastname'] = 'ahmed'
print(dict_copy)

my_dict.update(dict_copy) # merges to dictionary
print(my_dict)

x = my_dict['mother']['father']
print(x)
# print(x['father'])

