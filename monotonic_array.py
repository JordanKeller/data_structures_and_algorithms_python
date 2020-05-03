def is_monotonic(arr):

	"""Given an input array, output True or False depending
	upon array monotonicity."""

	monotone_increasing = True
	monotone_decreasing = True

	for i in range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			monotone_increasing = False
			break

	for i in range(len(arr) - 1):
		if arr[i] < arr[i + 1]:
			monotone_decreasing = False
			break

	return monotone_decreasing or monotone_increasing

# Test cases

A = [1, 2, 2, 3]

#print(is_monotonic(A))

B = [1, 3, 2]

#print(is_monotonic(B))

# O(len(arr)) complexity



