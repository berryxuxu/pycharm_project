class linked_list(object):
	class node():
		def __init__(self, value):
			self.value = value
			self.next = None
	def __init__(self):
		self.head = None
		self.tail = None
	def add(self, value):
		if self.head == None:
			self.head = self.node(value)
		else:
			temp = self.head
			while temp != None:
				temp = temp.next
				
	def __iter__(self):
		cursor = self.head
		while cursor != None:
			yield cursor.value
			cursor = cursor.next

a = linked_list()
a.add(1)
a.add(2)
a.add(3)
for i in a:
	print i


