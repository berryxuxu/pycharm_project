def bad_fabonacii(n):
    a = b =1
    if n == 1 or n == 2:
        return 1
    else:
        return bad_fabonacii(n-1) + bad_fabonacii(n-2)

def fabonacii2(n):
    a = b = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(n-2):
            a,b = b,a+b
        return b

def good_fabonacii(n):
    if n <= 1:
        return (n, 0)
    else:
        (a,b) = good_fabonacii(n-1)
        return (a+b, a)


print bad_fabonacii(5)
print fabonacii2(5)
print good_fabonacii(5)