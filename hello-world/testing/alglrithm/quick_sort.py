#coding:utf-8
#lis = [2,10,1,4,3,5,9]
import random
lis = [random.randrange(100) for i in range(10)]

def quick_sort(lis):
    less = [] #比pivot小的集合
    larger = [] #比pivot大的集合
    lenth = len(lis)
    if lenth <= 1:
        return lis
    for i in range(1, lenth):
        if lis[i] < lis[0]:
            less.append(lis[i])
        elif lis[i] >= lis[0]:
            larger.append(lis[i])
    print 'less',less
    print 'larger', larger
    print 'pivot', lis[0]
    print
    return quick_sort(less) + [lis[0]] + quick_sort(larger)


print 'Quick_sort:'
print quick_sort(lis)
