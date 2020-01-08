def selection_sort(data):
	"""Selection sort algorithm; input array data,
	output sorted array.  Always has O(n^2) performance;
	in-place and stable."""

	n = len(data)
	
	for i in range(n):
		min_entry = data[i]
		index = i
		for j in range(i, n):
			if data[j] < min_entry:
				min_entry = data[j]
				index = j

		data[i], data[index] = data[index], data[i]

	return data

a = [7, 6, 5, 4, 3]

#print(selection_sort(a))

def insertion_sort(data):
	"""Insertion sort algorithm; input array data, output
	sorted array.  Best case O(n), worst case O(n^2).
	In-place and stable."""

	n = len(data)

	for i in range(n):
		index = i
		for j in range(i):
			if data[i - 1 - j] > data[index]:
				data[index], data[i - 1 - j] = data[i - 1 - j], data[index]
				index = i - 1 - j
			else:
				break # allows for O(n) time best case.

	return data


#print(insertion_sort(a))

def bubble_sort(data):
	"""Bubble sort algorithm; input array data, output sorted
	array.  Always runs in O(n^2) time.  In-place and stable."""

	n = len(data)
	for i in range(n):
		for j in range(n - 1 - i):
			if data[j] > data[j + 1]:
				data[j], data[j + 1] = data[j + 1], data[j]


	return data

#print(bubble_sort(a))

def merge_sort(data, start, stop):
	"""Merge sort algorithm; input array data, output
	sorted array.  Worst case O(n ln n) performance.
	Not in-place, O(n) extra memory required.  Stable."""

	n = stop - start

	if n == 1:
		return

	m = start + n // 2

	merge_sort(data, start, m)
	merge_sort(data, m, stop)

	merge(data, start, stop)

def merge(data, start, stop):
	# utility function for merge_sort 
	# O(n) space required for allocation of temp array

	n = stop - start
	m = start + n // 2
	temp = [None] * n
	
	idx1 = start
	idx2 = m

	for i in range(n):

		if (idx1 < m and idx2 < stop):
			if data[idx1] < data[idx2]:
				temp[i] = data[idx1]
				idx1 += 1
			else:
				temp[i] = data[idx2]
				idx2 += 1
		elif idx1 == m:
			temp[i] = data[idx2]
			idx2 += 1
		elif idx2 == stop:
			temp[i] = data[idx1]
			idx1 += 1
		else:
			continue

	data[start:stop] = temp

#merge_sort(a, 0, 5)
#print(a)

from random import choice

def quick_sort(data):
	"""Quick sort algorithm; input array data, output
	sorted array.  Random pivot ensures average case
	O(n ln n) performance.  Worst case O(n^2).  Memory
	usage also has these characteristics, although an
	in-place implementation is possible."""

	if len(data) <= 1:
		return data

	pivot = choice(data)

	lesser_pivot = []
	equal_pivot = []
	greater_pivot = []

	for i in range(len(data)):
		if data[i] < pivot:
			lesser_pivot.append(data[i])
		elif data[i] == pivot:
			equal_pivot.append(data[i])
		else:
			greater_pivot.append(data[i])

	quick_sort(lesser_pivot)
	quick_sort(greater_pivot)

	for i in range(len(lesser_pivot)):
		data[i] = lesser_pivot[i]
	for j in range(len(equal_pivot)):
		data[len(lesser_pivot) + j] = equal_pivot[j]
	for k in range(len(greater_pivot)):
		data[len(lesser_pivot) + len(equal_pivot) + k] = greater_pivot[k]

	return data

#print(quick_sort(a))



# Add heap sort at some point.















