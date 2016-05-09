string = 'hart'
lis = []
for i in string:
    lis.append(i)

print lis
def cha(lis,lis1):

    for i in range(len(lis)):

        lis1.append(lis[i])
        print lis1
        if i <= len(lis)-2:
            cha(lis[1:],[])
        else:
            break
    return
print cha(lis,[])


