import copy
#print help(copy)
lis = [1,2,3]
lis1 = copy.deepcopy(lis)
lis2 = copy.copy(lis)
lis1.append(4)
lis.append(5)

print [0 for i in range(10)]
print [[0]*3 for i in range(10)]