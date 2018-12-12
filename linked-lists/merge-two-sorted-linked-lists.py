from pyllist import sllist, sllistnode


class List:
	""""custom singly linked list class """
	def __init__(self, data=0, next=None):
	    self.data = data
	    self.next = None

	def setData(self, newdata):
	    self.data = newdata

	def setNext(self, newnext):
	    # sets next node and pushes any connected next node as the next node of the new node
	    temp = self.next
	    self.next = newnext
	    newnext.next = temp

	def traverse(self):
	    node = self
	    while node != None:
	        print(node.data)
	        node = node.next
	    return

	def search(self, key):
	    # to look for a node within a linked list
	    node = self
	    while node != None:
	        node = node.next
	        if node == key:
	            break
	    return node

	def delete(self, node):
	    node.next = node.next.next



def merge_two_sorted_linked_list(llist_1, llist_2):
	""""
	this method uses custom linked list class	"""

	result_list = List()

	while llist_1 and llist_2:
		if llist_1.data < llist_2.data:
			result_list.next = llist_1
			llist_1 = llist_1.next
		else:
			result_list.next = llist_2
			llist_2 = llist_2.next

	return result_list


def merge_sorted_linked_list(first_list, sec_list):
	# This method uses the python module for linked list

	result_list = sllist()
	len_first = len(first_list)
	len_sec = len(sec_list)

	i = 0
	j = 0
	while i < len_first and j < len_sec:
		if first_list[i] < sec_list[j]:
			result_list.append(first_list[i])
			i+=1
		else: 
			result_list.append(sec_list[j])
			j+=1
	
	# add remaining items to the result_list. incomplete
	tail = i if i > j else j
	
	return result_list


if __name__ == '__main__':

	# test using custom singly linked list class
	llist_1 = List(2)
	nodellist_11 = List(5)
	nodellist_12 = List(7)
	llist_1.next = nodellist_11
	nodellist_11.next = nodellist_12

	llist_2 = List(3)
	nodellist_21 = List(11)
	llist_2.next = nodellist_21

	print('traversing LL #1')
	print(llist_1.traverse())

	print('traversing LL #2')
	print(llist_2.traverse())

	print('\nTraversing result_list:')
	print(merge_two_sorted_linked_list(llist_1, llist_2).traverse())



	# test using python module for linked list
	A = [2,5,7]
	B = [3,11]

	# initialize two sllist
	first_list = sllist(A)
	sec_list = sllist(B)

	print(merge_sorted_linked_list(first_list, sec_list))




