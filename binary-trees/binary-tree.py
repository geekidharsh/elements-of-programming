# -- project:
# -- @author: Harshvardhan Pandey

'''
tree is a ds composed of nodes
a node with no child nodes is called a 'leaf'


tree is implemented using: 
	1. dynamically storing node like a linked list. 
	2. using arrays: only for a complete binary tree.

'''

class BinaryTreeNode:
	"""docstring for BT Node"""
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right


# TRAVERSING OPERATION
def preorder(root):
	# preorder processes root before left and then finally right child
	if root:
		print(root.data)
		preorder(root.left)
		preorder(root.right)

def inorder(root):
	# inorder processes left then root and then finally right child
	if root:
		inorder(root.left)
		print(root.data)
		inorder(root.right)

def postorder(root):
	if root:
		postorder(root.right)
		postorder(root.left)
		print(root.data)


# TEST

# sample node a
a = BinaryTreeNode('parent')
a.left = BinaryTreeNode('left child')
a.right= BinaryTreeNode('right child')

print('sample print of nodes {} > {} > {}'.format(a.data, a.left.data, a.right.data))

# now creating a tree from the node a
preorder(a)
inorder(a)
postorder(a)





