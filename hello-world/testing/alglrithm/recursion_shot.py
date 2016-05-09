lis = [i for i in range(9)]
num = 0
def rec (summ, left):
    global num
    if left == 1:
        for i in  range(1,11):
            if summ + i == 90:
                num += 1
                return num

    for x in range(1,11):
        num += rec(summ, left-1)

    return num

print rec(0, 10)
