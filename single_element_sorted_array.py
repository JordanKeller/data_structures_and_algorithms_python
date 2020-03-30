def single_element_sorted(nums, start, stop):
	"""Given a sorted array, all values but one occur 
	exactly twice.  Return the index of the singleton element."""


	switch = (stop - start - 1) % 4

	mid = start + ((stop - start) // 2)

	if stop - start == 1:
		return start


	if switch == 0:
		if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
			return mid
		elif nums[mid] == nums[mid - 1]:
			return single_element_sorted(nums, start, mid +1)
		else:
			return single_element_sorted(nums, mid, stop)
	else:
		if nums[mid] == nums[mid - 1]:
			return single_element_sorted(nums, mid + 1, stop)
		else:
			return single_element_sorted(nums, start, mid)



# test cases:

a = [1, 1, 2, 3, 3, 4, 4, 8, 8]
b = [3, 3, 7, 7, 10, 11, 11]

#print(single_element_sorted(a, 0, len(a)))
#print(single_element_sorted(b, 0, len(b)))

# O(ln n) performance.






