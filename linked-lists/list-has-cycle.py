from listNode import ListNode

""""
1--> 2 --> 5 ->7
			^	|
			|	v
			3<--4
"""


def has_cycle(head):
	""""
	boolean function to identify a cycle in a linked list
	"""
	print('\nIn has_cycle')

	count = {}
	if head != None:
		while head:
			if head.next in count:
				return True
			else:
				count[head] = 1
				head = head.next
	return False
	# space complexity is O(n)


def cycle_len(end):
	start = end
	step = 0
	while True:
		start = start.next
		step += 1
		if start is end:
			return step


def has_cycle_inplace(head):
	print('\nIn has_cycle_inplace')
	if head:
		slow = fast = head
		while (fast != None) and (fast.next != None) and (fast.next.next):
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				print('Number of steps in in the cycle_len', cycle_len(slow))
				return True
		return False

		# time complexity is O(n^2) and space is O(1)


def main():
	# test
	A = ListNode('A')
	B = ListNode('B')
	C = ListNode('C')
	D = ListNode('D')
	E = ListNode('E')
	F = ListNode('F')
	G = ListNode('G')

	A.next, B.next, C.next, D.next, E.next, F.next = B, C, D, E, F, G
	G.next = B
	# print(A.traverse()) #this will enter a loop when linked list has a cycle

	print(has_cycle(A))
	print(has_cycle_inplace(A))



if __name__ == '__main__':
	main()



