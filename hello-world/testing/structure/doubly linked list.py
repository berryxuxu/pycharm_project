#coding=utf-8
class DoublyLinkedList(object):
    class _Node(object):
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element=None, prev=None, next=None):
            self._element = element
            self._prev = prev
            self._next = next
    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
    def insert(self,element):
        new = self._Node(element)
        if self._head._element == None:
            self._head = new
            self._tail = self._head
        elif self._head == self._tail:
            if element > self._head._element:
                self._tail = new
                self._head._next = self._tail
                self._tail._prev = self._head
            else:
                self._head = new
                self._head._next = self._tail
                self._tail._prev = self._head
        else:
            if element < self._head._element:
                new._next = self._head
                self._head._prev = new
                self._head = new
            elif element > self._tail._element:
                new._prev = self._tail
                self._tail._next = new
                self._tail = new
            else:
                cur = self._head
                while cur._next._element != None:
                    if cur._element <= element and cur._next._element >= element:
                        '''
                        先搞定插入节点的前后指针，其次是后节点的前指针，最后是前节点的后指针
                        '''
                        new._prev = cur
                        new._next = cur._next
                        cur._next._prev = new
                        cur._next = new
                        break
                    cur = cur._next
    def __iter__(self):
        cursor = self._head
        while cursor != None:
            yield cursor._element
            cursor = cursor._next

a = DoublyLinkedList()
a.insert(3)
a.insert(4)
a.insert(2)
a.insert(10)
a.insert(5)
a.insert(100)
a.insert(20)
a.insert(1)
for i in a:
    print i
