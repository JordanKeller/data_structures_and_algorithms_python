class DynamicArray:
	"""Dynamic array implementation in Python"""

	def __init__(self):

		self._data = [None]
		self._size = 0
		self._capacity = 1


	def __len__(self):

		return self._size

	def is_empty(self):

		return len(self) == 0

	def __getitem__(self, k):
		# Return the element at index k.

		if self._size <= k:
			raise Exception('Index out of range.')

		return self._data[k]

	def __setitem__(self, k, val):

		if self._size <= k:
			raise Exception('Index out of range.')

		self._data[k] = val

	def __iter__(self):

		for i in range(self._size):
			yield self._data[i]


	def push(self, val):
		"""Adds object to the end of the array.
		Enlarges array to twice its original size
		when self._size == self._capacity."""

		if self._size == self._capacity:

			self._enlarge()

		self._data[self._size] = val
		self._size += 1

	def pop(self):
		"""Removes and returns last element in the array.
		Shrinks array to half its original size when 
		self._size <= (1/4)self._capacity."""

		if self._size <= (1/4) * self._capacity:

			self._shrink()

		result = self._data[self._size - 1]
		self._data[self._size - 1] = None
		self._size -= 1
		return result

	def insert(self, k, val):
		"""Insert element with value val at the k-th index."""

		if k >= self._size:
			raise Exception('Index out of range.')

		#insert the value onto the end of the array
		self.push(val)

		#swap repeatedly to move the element to the k-th index
		for j in range(self._size - k - 1):
			idx = self._size - 1 - j
			self._data[idx], self._data[idx - 1] = self._data[idx - 1], self._data[idx]


	def delete(self, k):
		"""Removes the element at the k-th index, returning
		the same."""

		if k >= self._size:
			raise Exception('Index out of range.')

		# swap the element to the end of the array
		for j in range(k, self._size - 1):
			self._data[j], self._data[j + 1] = self._data[j + 1], self._data[j]

		return self.pop()

	def _enlarge(self):
		"""Utility function; doubles array capacity."""

		temp = [None] * (2 * self._capacity)

		for i in range(self._size):
			temp[i] = self._data[i]

		self._data = temp
		self._capacity *= 2


	def _shrink(self):
		"""Utility function; halves array capacity."""

		temp = [None] * int(((1/2) * self._capacity))

		for i in range(self._size):
			temp[i] = self._data[i]

		self._data = temp
		self._capacity = int((1/2) * self._capacity)



#d = DynamicArray()

#print(len(d))
#print(d.is_empty())

#d.push(3)
#d.push(4)
#d.push(5)

#d.insert(2, 17)

#d.delete(1)

#for x in d:
#	print(x)

#print(len(d))
#print(d.is_empty())

#d[2] = 6

#print(d[2])

#for x in d:
#	print(x)

#for i in range(len(d)):
#	print(d.pop())

#print(d.is_empty())
