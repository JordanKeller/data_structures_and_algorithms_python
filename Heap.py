class Heap:
	"""Minimum-oriented heap implementation in Python
	via dynamic array data structure (i.e., Python list)."""


	class _Node:

		__slots__ = ['_key', '_value'] # save namespace memory

		def __init__(self, key, value):
			self._key = key
			self._value = value

		def __eq__(self, other):

			if type(self) == type(other):
				return self._key == other._key

		def __lt__(self, other):

			if type(self) == type(other):
				return self._key < other._key

		def _get_key(self):

			return self._key 

		def _get_value(self):

			return self._value 

		def _get_item(self):
			return self._key, self._value


	def __init__(self):

		self._data = []
		self._size = 0


	def __len__(self):

		return self._size

	def is_empty(self):

		return len(self) == 0

	def __getitem__(self, k):

		if k >= self._size:
			raise Exception('Index out of range.')

		return self._data[k]._get_item()

	def __setitem__(self, k, key, value):
		"""implemented in child class
		AdjustablePriorityQueue"""
		
		raise ImplementationError('Method not implemented.')

	def _children(self, k):
		"""input index k, output indices for left and
		right children as tuple 
		left_children, right_children;
		returns None for absent children"""

		if k >= self._size:
			raise Exception('Index out of range.')

		left_child = None
		right_child = None

		if 2 * k + 1 < self._size:
			left_child = 2 * k + 1

		if 2 * k + 2 < self._size:
			right_child = 2 * k + 2

		return left_child, right_child

	def _parent(self, k):
		"""input index k, output index of parent;
		returns None for top of the heap/ heap root"""

		if k >= self._size:
			raise Exception('Index out of range.')

		if k == 0:
			return None

		parent = (k - 1) // 2
		return parent

	def get_min(self):

		if len(self) == 0:
			raise Exception('Empty heap.')

		return self[0]._get_item()


	def add_node(self, key, value):

		# add an element to the heap, maintaining
		# the heap ordering. O(ln n) speed (amortized)

		# add to the bottom of the heap
		self._data.append(self._Node(key, value))
		self._size += 1

		# regain heap ordering
		self._bubble_up(self._size - 1)

	def remove_min(self):

		# remove the minimum (top) element of the heap,
		# preserving the heap ordering along the way
		# O(ln n) speed (amortized)

		if self._size == 0:
			return

		if self._size == 1:
			self._size -= 1
			return self._data.pop()._get_item()

		# swap first and last elements
		self._swap(0, self._size - 1)
		# remove last element, now the minimal element
		result = self._data.pop()
		self._size -= 1


		# recover the heap ordering in the residual heap
		self._bubble_down(0)
	
		return result._get_item()

	def _bubble_up(self, k):
		"""Utility function for add method; restores
		heap ordering after addition of a new element."""

		parent = self._parent(k)

		if parent == None:
			return

		if self._data[parent] > self._data[k]:
			self._swap(k, parent)
			self._bubble_up(parent)


	def _bubble_down(self, k):
		"""Utility function for remove_min method;
		preserves heap ordering during removal of minimal
		element (at the top of the heap)."""

		left_child, right_child = self._children(k)

		if left_child == None:
			return

		smallest_child = left_child

		if right_child != None and self._data[right_child] < self._data[left_child]:
			smallest_child = right_child

		if self._data[k] > self._data[smallest_child]:
			self._swap(k, smallest_child)
			self._bubble_down(smallest_child)


	def _swap(self, k, l):
		"""Utility function for remove_min, _bubble_up,
		and _bubble_down methods."""

		if k >= self._size or l >= self._size:
			raise Exception('Index out of range.')

		self._data[k], self._data[l] = self._data[l], self._data[k]


#POW = 4
#sz = 2 ** POW - 1

#for i in range(sz):
#	H.add_node(sz - i, i)


#for i in range(len(H)):
#	print(H[i])


def heap_sort(data):
	"""Heap-based sorting algorithm.  Input an 
	array, output sorted array.  Performance is
	O(n ln n), requires O(n) additional memory.
	An in-place version is possible."""

	n = len(data)
	H = Heap()

	if n <= 1:
		return

	for i in range(len(data)):
		H.add_node(data[i], data[i])
	# O(n ln n) total operations; more efficient
	# to use heapify for O(n) heap construction

	for i in range(len(data)):
		data[i] = H.remove_min()[0]
	# O(n ln n) total operations

	return data

sz = 10

data = [sz - i for i in range(sz)]

print(heap_sort(data))






















