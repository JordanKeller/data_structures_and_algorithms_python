import DoublyLinkedList as DL
# relies upon the file DoublyLinkedList.py

class LinkedListQueue(DL.DoublyLinkedList):
	"""Linked list based queue implementation.  Supports
	enqueue and dequeue methods with O(1) speed."""

	def __init__(self):
		super().__init__()

	def get_head(self):
		return super().get_head()

	def enqueue(self, val):
		self.add_to_tail(val)

	def dequeue(self):
		return self.remove_from_head()


# add a queue class built upon dynamic array structure


Q = LinkedListQueue()

Q.enqueue(5)
Q.enqueue(6)
Q.enqueue(7)

#print(Q.get_head())

#print(Q.dequeue())
#print(Q.dequeue())
#print(Q.dequeue())
#print(Q.get_head())
#Q.dequeue()