import Heap

class AdjustablePriorityQueue(Heap.Heap):
	"""Heap based implementation of a minimum-oriented
	adjustable priority queue.  remove_min and add_node
	methods have amortized O(ln n) performance"""

	def __init__(self):
		super().__init__()

	def __setitem__(self, k, item):
		"""Adjust an index's (key, value) pair,
		restoring the heap ordering afterward
		via the _bubble_up or _bubble_down methods."""

		temp = self._data[k]
		self._data[k] = self._Node(item[0], item[1])

		if self._data[k] < temp:
			self._bubble_up(k)
		elif self._data[k] > temp:
			self._bubble_down(k)
		else:
			return

	def get_min(self):

		return super().get_min()

	def remove_min(self):

		return super().remove_min()

	def add_node(self, key, value):

		super().add_node(key, value)




H = AdjustablePriorityQueue()

POW = 4
sz = 2 ** POW - 1

#for i in range(sz):
#	H.add_node(sz - i, i)


#H[5] = (-99, 'T')

#for i in range(len(H)):
#	print(H[i])





