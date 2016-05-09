import random

row, column = random.randrange(0,3), random.randrange(0,3)
print row, column

scores = [[0 for i in range(3)]
              for ii in range(3)]
print scores

for _ in range(4):
    print 'a'
