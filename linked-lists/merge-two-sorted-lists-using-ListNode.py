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



def merge_two_sorted_lists(L1, L2):

    # Creates a placeholder for the result.
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Appends the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next



# test
L1 = ListNode(2, ListNode(5, ListNode(7)))
L2 = ListNode(3, ListNode(11))

print(L1.traverse(), L2.traverse())

merged_List = merge_two_sorted_lists(L1, L2)
print(merged_List.traverse())


