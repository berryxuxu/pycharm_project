class name(object):
    ABC =  0
    def __init__(self):
        self.a = self.ABC + 1
        pass
    pass

a = name()
print a.ABC
print a.a
print type(a)

