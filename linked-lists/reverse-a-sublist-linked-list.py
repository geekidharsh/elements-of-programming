class ListNode:
	"""docstring for ListNode. 
	implementing a singly linked list class"""


	def __init__(self, data=0, next=None):
		self.data = data
		self.next = next

	def search_list(L, key):
		while L and L.data != key:
			L = L.next
			# if key is not present then None will return
		return L

	def insert_after(node, newnode):
		newnode.next = node.next
		node.next = newnode

	def delete_after(node):
		node.next = node.next.next

	def traverse(node):
		items = []
		while node != None:
			items.append(node.data)
			node = node.next
		return items


""""solution"""

# test
L1 = ListNode(2, ListNode(5, ListNode(7, ListNode(3, ListNode(11, ListNode(13))))))
# print(L1.traverse())


def reverse_a_sublist(L1, start, finish):
	# start and finish are integer numbers denoting the position in linked list. 
	# head node being starting from 1 in this case. 
	start_head = ListNode(0, L1)
	dummy_head = start_head

	i = 1
	for i in range(1, start):
		start_head = start_head.next

	sublist_iter = start_head.next

	for i in range(finish-start):
		temp = sublist_iter.next
		print(start_head.traverse(),sublist_iter.traverse() , temp.traverse())
		sublist_iter.next = temp.next
		temp.next = start_head.next
		start_head.next = temp

	return dummy_head.next.traverse()
		
print(L1.traverse())
print(reverse_a_sublist(L1, 3,5))












