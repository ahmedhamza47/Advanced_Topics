
first_name = 'hamza'
last_name = 'ahmed'

full_name = first_name + ' ' + last_name
print(full_name)

if 'h' in first_name:
    print('yes')
else:
    print('no')

sentence = '     hello world     '
print(sentence)
sentence = sentence.strip()  # removes the blank spaces
print(sentence)

print(sentence.startswith('hello'))
print(sentence.endswith('hello'))

print(sentence.replace('hello','hi'))

# to convert a string into a list
my_list = sentence.split()
print(my_list)
# to convert list into string
string = ' '.join(my_list)
print(string)

# formatted string(old style)
digits = 27.78932
print('my digit is %.2f' % digits)

# formatted string(medium style)
print('my digit is {:.2f}'.format(digits))
digits2 = 3.143
print('my new digits are {:.2f} and {}'.format(digits,digits2))

# formatted string(above pyton 3.6)
print(f'my new digits are{digits:.2f} and {digits2}')