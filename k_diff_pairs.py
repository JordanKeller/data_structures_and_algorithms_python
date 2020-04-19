def num_counts(nums):
	"""Utility dictionary with keys as array entries, values
	as their frequency in the array."""

	result = {}
	for i in range(len(nums)):
		result[nums[i]] = result.get(nums[i], 0) + 1

	return result


def k_diff_pairs(nums, k):

	"""Input an array of integers and an integer k, output the total
	number of unique pairs in the array with difference k."""


	if k < 0:
		return 0

	helper_dict = num_counts(nums)

	count = 0
	if k == 0:
		for x in helper_dict.keys():
			if helper_dict[x] >= 2:
				count += 1

		return count
	else:
		for x in helper_dict.keys():
			if helper_dict.get(x + k, 0) != 0:
				count += 1
			if helper_dict.get(x - k, 0) != 0:
				count += 1

		return count // 2 # handshake lemma


# O(len(nums)) performance

# Test cases

nums = [3, 1, 4, 1, 5]
k = 2

#print(k_diff_pairs(nums, k))

nums = [1, 2, 3, 4, 5]
k = 1

#print(k_diff_pairs(nums, k))













