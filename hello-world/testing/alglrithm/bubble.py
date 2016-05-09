lis = [5,4,3,2,1]
import random
lis = [random.randrange(100) for i in range(10)]

def bubble(lis):
    out = 0  # number of numbers that have been sorted
    lenth = len(lis)
    if lenth <= 1:
        return lis
    while out < lenth-1:
        for n in range(lenth-1):
            if lis[n] > lis[n+1]:
                lis[n], lis[n+1] = lis[n+1], lis[n]
        print lis
        out += 1
    return lis

print 'Bubble:' , bubble(lis)

