class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
	
	def __str__(self):
		return self.value
	
# bfs that reverses every other line
def traverse(root):
	visited = []
	q = [root]
	count = 0
	while q:
		nex_q = []
		new_visited = []
		for node in q:
			new_visited.append(node.value)
			if node.left:
				nex_q.append(node.left)
			if node.right:
				nex_q.append(node.right)
		if not count%2:
			new_visited.reverse()
		visited += new_visited
		count+=1
		q = nex_q
	return visited

node9 = Node("Node9", None, None)
node10 = Node("Node10", None, None)
node7 = Node("Node7", None, None)
node8 = Node("Node8", node9, node10)
node5 = Node("Node5", None, None) 
node6 = Node("Node6", node7, node8)
node3 = Node("Node3", None, None)  
node4 = Node("Node4", node5, node6)
node1 = Node("Node1", node3, node4)
node2 = Node("Node2", None, None)  
root = Node("Root", node1, node2)
for v in traverse(root):
	print(v)