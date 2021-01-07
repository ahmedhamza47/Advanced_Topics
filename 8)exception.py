
# x = -5
# if x<0:
#     raise Exception('x should be positive')


try:
    y = 3 / 0

except ZeroDivisionError:  # or except Exception as e:
    print('error')          # print(e) output: zero division error

print('process ended')

try:
    x = 3/0
except Exception as e:
    print(e)

else:                           # if exception does not occur then this part is executed
    print('no errors generated')
finally:                        # this method runs no matter if error occur or not
    print('success')


