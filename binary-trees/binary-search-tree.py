"""a binary search tree, in which for every node x 
and it's left and right nodes y and z, respectively.
y <= x >= z"""

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



# SEARCH in a Binary search tree

def bst_search_recursive(root, key):
	if key == root.data or root is None:
		return root	 
	if key < root.data:
		return bst_search_recursive(root.left, key)
	if key > root.data:
		return bst_search_recursive(root.right, key)



# TEST
# ----

# sample node a
a = BinaryTreeNode(18)
a.left = BinaryTreeNode(15)
a.right= BinaryTreeNode(21)


# TRAVERSING a binary search tree
inorder(a)
preorder(a)
postorder(a)


# searching
print(bst_search_recursive(a, 14))




