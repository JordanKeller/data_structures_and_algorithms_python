import DoublyLinkedList as DL
# relies upon the file DoublyLinkedList.py 

class LinkedListStack(DL.DoublyLinkedList):
	"""Linked list based stack implementation.  Supports
	push and pop methods with O(1) speed."""


	def __init__(self):

		super().__init__()


	def get_top(self):
		return self.get_head()


	def push(self, val):

		self.add_to_head(val)


	def pop(self):

		return self.remove_from_head()





S = LinkedListStack()

S.push(5)
S.push(6)
S.push(7)
#print(S.is_empty())

#S.pop()
#print(S.get_top())
#S.pop()
#S.pop()
#print(S.get_top())

#print(S.pop(), S.pop(), S.pop())
#print(S.is_empty())

#for x in S:
#	S.pop()


#print(S.is_empty())