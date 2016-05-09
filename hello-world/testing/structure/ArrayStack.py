class ArrayStack(object):
    def __init__(self, lis=[]):
        self.data = lis

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else: return False

    def push(self, val):
        self.data.append(val)

    def top(self):
        if self.is_empty() == True:
            raise ValueError('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty() == True:
            raise ValueError('Stack is empty')
        self.data.pop()


s = ArrayStack([1,3,5])
print s.data
