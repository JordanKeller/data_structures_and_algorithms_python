def missing_number(arr):

	"""Given a length n array containing n distinct numbers from 
	0, 1,..., n, find the missing value."""


	n = len(arr)
	total = sum(arr)

	return (n * (n + 1) // 2) - total


# Test cases
A = [3, 0, 1]

print(missing_number(A))

B = [9, 6, 4, 2, 3, 5, 7, 0, 1]

print(missing_number(B))

# O(n) complexity