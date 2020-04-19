

def lca(node0, node1):
	iter0, iter1 = node0, node1
	nodes_on_path_to_root = set()

	while iter0 or iter1:
		# move upwards in tandem for each nodes

		if iter0:
			if iter0 in nodes_on_path_to_root:
				return iter0
			nodes_on_path_to_root.add(iter0)
			iter0 = iter0.parent()

		if iter1:
			if iter1 in nodes_on_path_to_root:
				return iter1
			nodes_on_path_to_root.add(iter1)
			iter1 = iter1.parent()
	raise ValueError('Either of the nodes not in given tree')


# time: o(d0+d1) where d0 and d1 is the depth of each node from node to ancestor
# worst case: o(h) where h is the height of the tree

# space: o(d0 + d1)

