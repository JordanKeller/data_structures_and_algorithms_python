def bin_search(nums, target, start, stop):
	"""Binary search helper function."""

	n = stop - start
	m = start + n // 2

	if n == 0:
		return [-1, -1]

	if n == 1:
		if nums[start] == target:
			return start
		else:
			return -1

	if nums[m] == target:
		return m
	elif nums[m] > target:
		return bin_search(nums, target, start, m)
	else:
		return bin_search(nums, target, m, stop)


def search_range(nums, target):

	"""Given a sorted array and an array entry as input, output
	the indices corresponding to this array entry."""


	if len(nums) == 0:
		return [-1, -1]


	first = bin_search(nums, target, 0, len(nums))
	last = first

	if first == -1:
		return [-1, -1]

	i = first - 1
	j = last + 1

	# some sort of binary search in remaining halves?
	# the following linear search has to be suboptimal
	# in the worst case.

	while (i >= 0) and nums[i] == target:
		i -= 1

	while (j < len(nums)) and nums[j] == target:
		j += 1

	first = i + 1
	last = j - 1

	return [first, last]


nums = [5, 7, 7, 8, 8, 10]
target = 8

print(search_range(nums, target))

target = 6

print(search_range(nums, target))

























