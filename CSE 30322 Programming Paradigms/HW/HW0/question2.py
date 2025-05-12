from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def text_to_list(expression: str) -> list:
  # save string up until '+','-','*','/' and add both that str as int as a node and symbol to the list
  value = ''
  nodes = []
  for c in expression:
    # modified code start
    if c in ['+','-','*','/'] and value != '':
    # modified code end
      nodes.append(TreeNode(int(value)))
      nodes.append(TreeNode(c))
      value = ''
    else:
      value+=c
      
  # add the final number
  nodes.append(TreeNode(int(value)))
  return nodes

def list_to_tree(nodes: list) -> TreeNode:
  # first parse: make a new list that combines all the subtrees of * and /
  new_nodes = []
  n = len(nodes)
  i = 0
  while i < n:
    if nodes[i].val in ['*','/']:
      nodes[i].left = new_nodes.pop()
      nodes[i].right = nodes[i+1]
      new_nodes.append(nodes[i])
      i+=2
    else:
      new_nodes.append(nodes[i])
      i+=1

  # second parse: make a new list that combines all the subtrees of + and -
  nodes = new_nodes
  new_nodes = []
  n = len(nodes)
  i = 0
  while i < n:
    if nodes[i].val in ['+','-']:
      nodes[i].left = new_nodes.pop()
      nodes[i].right = nodes[i+1]
      new_nodes.append(nodes[i])
      i+=2
    else:
      new_nodes.append(nodes[i])
      i+=1
  return new_nodes[0]


def tree_to_list(root: TreeNode) -> list:
  # bfs traversal to print out children of each node
  q = deque([root])
  res = []
  while q:
    node = q.popleft()
    if node.left:
      q.append(node.left)
      res.append(f'"{node.val}" -> "{node.left.val}" // left')
      q.append(node.right)
      res.append(f'"{node.val}" -> "{node.right.val}" // right')
  return res

def text_to_tree(expression: str) -> list:
  # ... solution here ...
  nodes = text_to_list(expression) # converts string into a list of nodes, node val: num or sign
  root = list_to_tree(nodes) # converts the list of nodes into binary expression tree
  return tree_to_list(root) # returns the in-order traversal of nodes


def print_output(output: list) -> None:
    for line in output:
        print(line)

def test(expression):
  output = text_to_tree(expression)
  print_output(output)
  print()

if __name__ == "__main__":
  test("2*7+3")                   # Test 1
  test("8/2*10")                  # Test 2
  test("8/2/10")                  # Test 3
  test("2*7+3*8")                 # Test 4
  test("2+7*3*8")                 # Test 5
  test("7*3*8+2")                 # Test 6
  test("8+2+10+100*6-10/30+7")    # Test 7
  test("10+5-3")                  # Test 1
  test("-2*7+3")                   # Test 1
  