class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


def avg_levels_binary_tree(root):

	"""Given a binary tree as input, calculate the average values of each
	of its levels, output as an array."""

	node_list = collections.deque() # helpful in BFS-style approach
	node_list.append(root)
	level_avgs = []
	while node_list != []:
		tot = 0
		n = len(node_list)
		for i in range(n):
			temp = node_list.popleft() 
			if temp.left:
				node_list.append(temp.left)
			if temp.right:
				node_list.append(temp.right)
		level_avgs.append(tot / n)


	return level_avgs

# Test cases...

# Complexity ought to be O(V).  Recall that no. edges can be estimated
# by no. of vertices in binary case.


