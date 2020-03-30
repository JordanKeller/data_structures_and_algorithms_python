def find_max_average_sub(nums, k):

	"""Given an array of nums, return the largest average
	value of a continuous subarray of length k."""


	result = sum(nums[:k]) / k
	current = result

	for i in range(1, len(nums) - k + 1):

		current = (current * k - nums[i - 1] +\
		 nums[i + k - 1]) / k

		if result < current:
			result = current


	return result

# test cases

a = [1, 12, -5, -6, 50, 3]
k = 4

print(find_max_average_sub(a, k))

# O(n) rather than the naive O(n * k)
