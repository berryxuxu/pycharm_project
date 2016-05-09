class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.pointer = 0
        self.con = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.con.append(x)
        self.pointer += 1
        return
    
    def pop(self):
        """
        :rtype: nothing
        """
        self.con.pop()
        self.pointer -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.con[self.pointer-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.con) == 0:
            return
        lis = MinStack()
        lis.push(self.con[self.pointer-1])
        self.pop()
        while self.pointer > 0:
            if  self.con[self.pointer-1] <= lis.top:
                lis.push(self.con[self.pointer-1])
            self.pointer -= 1
        return lis.top    

a = MinStack()
print a.push(-3)
print a.getMin()