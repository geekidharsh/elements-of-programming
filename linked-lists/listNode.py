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

if __name__ == '__main__':
	main()