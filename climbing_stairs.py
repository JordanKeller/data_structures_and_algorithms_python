def climbing_stairs(n):

	"""Input a positive integer n.  Climb n steps, taking either a single
	stair or two stairs with each step.  Output the distinct ways to
	climb to the top of the stairs."""

	a = 1
	b = 2

	if n == 1:
		return a
	if n == 2:
		return b

	# n >= 3

	for i in range(n - 2):
		c = a + b
		a = b
		b = c

	return b

# O(n) complexity.  The Fibonacci sequence in disguise, since
# the count C(n) satisfies the Fibonacci recursion formula:
# F(n) = F(n - 1) + F(n - 2).

