#coding:utf-8
#lis = [2,10,1,4,3]
import random
lis = [random.randrange(100) for i in range(10)]
print lis
def merge_sort(lis):
    lenth = len(lis)
    mid = lenth/2
    if mid == 0 :
        return lis
    else:
        lis1 = lis[:mid]
        lis2 = lis[mid:]
        lis1 = merge_sort(lis1)
        lis2 = merge_sort(lis2)
        re_lis = merge(lis1, lis2)
        print re_lis
    return re_lis
def merge(lis1, lis2):
    '''
    merger two sorted list into one.
    '''
    lis = []
    len1 = len(lis1)
    len2 = len(lis2)
    p1 = p2 = 0   #指针(pointer)

    for i in range(len1 + len2):
        if p1 >= len1 or p2 >= len2:
            break
        if lis1[p1] < lis2[p2]:
            lis.append(lis1[p1])  #因为两个lis已经sort好了，所以只要比较两个lis的第一个谁小，就是最小的
            p1 += 1
        else:
            lis.append(lis2[p2])
            p2 += 1
    if p1 < len1: #把剩下的都加到lis里面
        for i in range(len1-p1):
            lis.append(lis1[p1+i])
    if p2 < len2:
        for i in range(len2-p2):
            lis.append(lis2[p2+i])
    print 'lis',lis
    return lis
print merge_sort(lis)