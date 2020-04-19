def num_counts(a):
	"""Helper dictionary counting occurences of the array entries."""

	result = {}
	for x in a:
		result[x] = result.get(x, 0) + 1

	return result


def array_intersection(nums1, nums2):
	"""Input two arrays, output their intersection.  Each element 
	in the output should be unique."""

	d1 = num_counts(nums1)

	intersection = []

	for x in nums2:
		if d1.get(x, 0) != 0:
			d1[x] = 0
			intersection.append(x)

	return intersection

# O(len(nums1) + len(nums2)) complexity

# Test cases...

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

#print(array_intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

#print(array_intersection(nums1, nums2))









