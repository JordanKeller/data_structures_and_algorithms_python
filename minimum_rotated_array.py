def find_min(nums, start, stop):
	"""Input a rotation of a sorted array, 
	output the minimum value."""

	if stop - start == 0:
		return nums[start]

	if stop - start == 1:
		if nums[start] < nums[stop]:
			return nums[start]
		else:
			return nums[stop]


	mid = start + ((stop - start) // 2)

	if nums[start] < nums[mid] < nums[stop]:
		return nums[start]
	elif nums[mid] < nums[stop] < nums[start]:
		return find_min(nums, start, mid)
	elif nums[stop] < nums[start] < nums[mid]:
		return find_min(nums, mid, stop)


# test cases

a = [3, 4, 5, 1, 2]
b = [4, 5, 6, 7, 0, 1, 2]

print(find_min(a, 0, len(a) - 1))
print(find_min(b, 0, len(b) - 1))


# O(ln n) performance
