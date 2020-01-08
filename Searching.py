def binary_search(data, val, start, stop):
	"""Binary search algorithm.  Input a sorted array
	and a value, return the index of that value within the array."""


	n = stop - start
	m = start + n // 2

	if n == 1:
		if data[start] == val:
			return start
		else:
			return None


	if data[m] == val:
		return m
	elif data[m] > val:
		return binary_search(data, val, start, m)
	else:
		return binary_search(data, val, m, stop)



a = [2, 3, 4, 5, 6]

#print(binary_search(a, 5, 0, 5))
#print(binary_search(a, 17, 0, 5))

from random import choice

def quick_select(data, k):
	"""Quick select algorithm; input array and value k,
	output the k-th order statistic of the input array
	(i.e., the k-th smallest value).  Random pivot ensures
	average case O(n) performance.  Worst case is O(n^2).
	Space requirements have the same characteristics."""

	n = len(data)

	if k > n:
		raise Exception('Order statistic out of range.')

	pivot = choice(data)

	lesser_pivot = []
	equal_pivot = []
	greater_pivot = []

	for i in range(n):
		if data[i] < pivot:
			lesser_pivot.append(data[i])
		elif data[i] == pivot:
			equal_pivot.append(data[i])
		else:
			greater_pivot.append(data[i])

	if k <= len(lesser_pivot):
		return quick_select(lesser_pivot, k)
	elif len(lesser_pivot) < k <= (len(lesser_pivot) + len(equal_pivot)):
		return equal_pivot[0]
	else:
		return quick_select(greater_pivot, (k - len(lesser_pivot) - len(equal_pivot)))


b = [7, 6, 5, 4, 3]

#print(quick_select(b, 4))
#print(quick_select(b, 17))
















