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






