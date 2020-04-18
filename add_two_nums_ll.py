class ListNode:

	def __init__(self, x):
		self.val = x
		self.next = None


def add_two_nums(l1, l2):

	"""Input two non-empty linked lists, representing two
	non-negative integers with digits stored in reverse order.
	Add the two numbers and output as a linked list with the
	same reverse ordering."""

	tot = l1.val + l2.val
	if tot >= 10:
		tot -= 10
		remainder = 1
	else:
		remainder = 0


	head = ListNode(tot)
	current = head
	temp1 = l1.next
	temp2 = l2.next

	while temp1 != None and temp2 != None:
		tot = temp1.val + temp2.val + remainder
		if tot >= 10:
			tot -= 10
			remainder = 1
		else:
			remainder = 0
		temp_node = ListNode(tot)
		current.next = temp_node
		temp1 = temp1.next
		temp2 = temp2.next


	while temp1 != None:
		tot = temp1.val + remainder
		if tot >= 10:
			tot -= 10
			remainder = 1
		else:
			remainder = 0
		temp_node = ListNode(tot)
		current.next = temp_node
		current = temp_node
		temp1 = temp1.next

	while temp2 != None:
		tot = temp2.val + remainder
		if tot >= 10:
			tot -= 10
			remainder = 1
		else:
			remainder = 0
		temp_node = ListNode(tot)
		current.next = temp_node
		current = temp_node
		temp2 = temp2.next

	if remainder == 1:
		current.next = ListNode(remainder)

	return head

# Test cases...

# Complexity O(max(len(l1), len(l2)))







