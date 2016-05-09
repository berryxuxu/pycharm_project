lis = [[21,22,4,5,6],[20,7,8,9,10],[19,6,1,2,11],[18,5,4,3,12],[17,16,15,14,13]]
for ii in lis:
    print ii

def found_num(x, y):
    return lis[x-1][y-1]

print found_num(1,2)

