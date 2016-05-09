#coding:utf-8
import random, copy
lis = [random.randrange(100) for i in range(10)]
lis1 = copy.deepcopy(lis)
print lis
lis1.sort()
print lis1

def insert_sort(lis):
    length = len(lis)
    for i in range(1,length): #从第二个开始循环
        if lis[i] < lis[i-1]:
            temp = lis[i]  #当前要插入的值
            for ii in range(i-1,-1,-1):
                if temp < lis[ii]:
                    lis[ii+1] = lis[ii] #右移
                else:
                    a = ii+1 #当前值应该插入的位置
                    break
            lis[a] = temp
    return lis

print insert_sort(lis)