a = '1 * 2 + (3+4)'


def stack_cal(a):
    lis = []
    for i in range(len(a)):
        if a[i] == '(':
            n = i+1
            while a[n] != ')'and n <= len(a)-1:
                lis.append(a[n])
                n += 1
        else:
            continue
    for i in range(len(lis)):
        if not lis[i].isdigit():
            if lis[i] == '+':
                return int(lis[i-1]) + int(lis[i+1])

print stack_cal(a)


