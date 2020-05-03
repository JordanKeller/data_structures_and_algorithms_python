import math

def bin_rep(num):

	if num < 0:
		raise Exception('Non-negative integers only.')

	if num == 0 or num == 1:
		return [num]

	exp = math.floor(math.log(num, 2))
	total = num
	result = []

	while total > 0:

		if total >= 2 ** exp:
			total -= 2 ** exp
			result.append(1)

		else:
			result.append(0)

		exp -= 1

	while exp >= 0:
		result.append(0)
		exp -= 1

	return result




def binary_complement(num):

	bin_list = bin_rep(num)
	n = len(bin_list)

	total = 0

	for i in range(n):
		total += ((bin_list[i] + 1) % 2) * (2 ** (n - 1 - i))

	return total


a = 5

#print(binary_complement(a))

b = 1

#print(binary_complement(b))






