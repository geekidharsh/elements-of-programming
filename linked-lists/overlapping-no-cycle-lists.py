from listNode import ListNode

""""
overlapping listNode:
L1 has a node that's also common to L2 but not a cycle.
"""


def main():
	# test
	A = ListNode('A')
	B = ListNode('B')
	C = ListNode('C')
	D = ListNode('D')
	E = ListNode('E')
	F = ListNode('F')
	G = ListNode('G')
	H = ListNode('H')
	I = ListNode('I')
	A.next, B.next, C.next, D.next = B, C, D, E
	# E.next, F.next = F, D
	print(A.traverse())
	print(E.traverse())



if __name__ == '__main__':
	main()