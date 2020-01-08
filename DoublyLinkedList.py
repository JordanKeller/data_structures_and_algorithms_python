class DoublyLinkedList:

	class _Node:

		def __init__(self, val, predecessor, successor):

			self._element = val
			self._prev = predecessor
			self._next = successor

		def get_element(self):

			return self._element

	def __init__(self):

		self._head = self._Node(None, None, None)
		self._tail = self._Node(None, None, None)
		self._head._next = self._tail
		self._tail._prev = self._head
		self._size = 0
		# use of sentinel head and tail nodes

	def __len__(self):

		return self._size

	def is_empty(self):

		return len(self) == 0

	def __getitem__(self, k):

		temp = self._head._next
		for i in range(k):
			temp = temp._next

		return temp.get_element()

	def __iter__(self):

		for k in range(len(self)):
			yield self[k]

	def get_head(self):

		return self._head._next.get_element()

	def get_tail(self):

		return self._tail._prev.get_element()


	def add_to_head(self, val):

		temp = self._Node(val, self._head, self._head._next)
		self._head._next._prev = temp
		self._head._next = temp
		self._size += 1

	def remove_from_head(self):

		if len(self) == 0:
			raise Exception('Empty DLL.')

		temp = self._head._next
		self._head._next._next._prev = self._head
		self._head._next = self._head._next._next
		self._size -= 1

		return temp.get_element()

	def add_to_tail(self, val):

		temp = self._Node(val, self._tail._prev, self._tail)
		self._tail._prev._next = temp
		self._tail._prev = temp
		self._size += 1

	def remove_from_tail(self):

		if len(self) == 0:
			raise Exception('Empty DLL.')

		temp = self._tail._prev
		self._tail._prev._prev._next = self._tail
		self._tail._prev = self._tail._prev._prev
		self._size -= 1

		return temp.get_element()


	# add methods for arbitrary insertion/deletion



S = DoublyLinkedList()
S.add_to_head(5)
S.add_to_head(6)
S.add_to_head(7)

#print(S.get_head())
#print(S.get_tail())



#print(S.remove_from_head(), S.remove_from_head())
#print(S.remove_from_tail(), S.remove_from_tail())

#for x in S:
#	print(x)

















