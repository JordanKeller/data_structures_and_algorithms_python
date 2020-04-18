def num_counts(arr):

	result = {}
	for i in range(len(arr)):
		result[arr[i]] = result.get(arr[i], 0) + 1

	return result

def lucky_number(arr):

	"""Input an array, output the largest lucky number in the array,
	defined as an entry with frequency equal to its value."""

	helper_dict = num_counts(arr)

	lucky_nums = []

	for x in helper_dict.keys():
		if x == helper_dict[x]:
			lucky_nums.append(x)

	if lucky_nums == []:
		return -1
	else:
		return max(lucky_nums)



# Test cases

arr = [2, 2, 3, 4]

#print(lucky_number(arr))

arr = [1, 2, 2, 3, 3, 3]

#print(lucky_number(arr))


# O(n) complexity, with n = len(arr).
# O(n) space requirement with num_counts dictionary