import copy
# shallow copying is only one level deep
original = [1,2,3,4,5]
cpy = original.copy()
cpy[0] = 10
print(original)
print(cpy)

org2 = [[1,2,3,4,5],[6,7,8,9,19]]
cpy1 = org2.copy()
cpy1[0][1] = 20
print(org2)
print(cpy1)  # both org2 and cpy1 has same value cuz shallow copy is one level deep

# so to make a deep copy we use
cpy2 = copy.deepcopy(org2)
cpy2[0][1] = 30
print(org2)
print(cpy2)

