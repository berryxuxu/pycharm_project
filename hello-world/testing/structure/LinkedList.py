#coding:utf-8
class LinkedList(object):
    class _Node(object):
        __slots__ = 'value', 'next'
        def __init__(self, value):
            self.value = value
            self.next = None
    def __init__(self, head = None):
        if head != None:
            self.head = self._Node(head)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None
    def append(self, value):
        if self.head == None:
            self.head = self._Node(value)
            self.tail = self.head
        elif self.tail != None:
            self.tail.next = self._Node(value)
            self.tail = self.tail.next
        else:
            self.tail = self._Node(value)
    def __iter__(self):
        cursor = self.head
        while cursor != None:
            yield cursor.value
            cursor = cursor.next

lis = LinkedList()
lis.append(1)
lis.append('a')
for i in lis:
    print i
