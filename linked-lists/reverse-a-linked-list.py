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


def reverse_a_sublist(head):
	# start and finish are integer numbers denoting the position in linked list. 
	# head node being starting from 1 in this case.
	curr = head
	prev = None

	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt

	return prev





		
print(L1.traverse())
print('\nAfter reverse')
print(reverse_a_sublist(L1).traverse())












