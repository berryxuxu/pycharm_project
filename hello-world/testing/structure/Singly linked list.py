class Link_list(object):
    class Node(object):
        def __init__(self, value = None):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = self.Node()
        self.head.next = None

    def __iter__(self):
        cur = self.head
        while cur != None:
            yield cur.value
            cur = cur.next

    def get_head(self):
        return self.head

    def get_tail(self):
        h = self.head
        while h.next != None:
            h = h.next
        return h

    def insert_to_last(self, value):
        node = self.Node(value)
        if self.head.value == None:
            self.head = node
        else:
            a = self.head
            while a.next != None:
                a = a.next
            a.next = node
        node.next = None

    def has_cycle(self):
        """
        time complexity : O(n^2)
        itype head: ListNode, rtype: bool
        """
        p1 = self.head
        while p1 != None:
            p2 = self.head
            while p2 != None:
                if p2 == p1.next:
                    return True
                if p2 == p1:
                    break
                else:
                    p2 = p2.next
            p1 = p1.next
        return False

lis = Link_list()
lis.insert_to_last(2)
lis.insert_to_last(4)
lis.insert_to_last(1)

for i in lis:
    print i

