def tree_to_text(tree, root_node):
  # your implementation here
  # your function will return a string!

  # create empty string and do an inorder traversal of the tree and add each element to string
  res = ""
  def dfs(cur):
    if not cur:
      return
    nonlocal res
    c = tree[cur]
    if not c:
      c = [None,None]
    dfs(c[0])
    i = 0
    # modified code start
    while cur[i] != '_':
      i+=1
    res+=cur[i+1:]
    # modified code end
    dfs(c[1])
  dfs(root_node)
  return res

if __name__ == "__main__":
  t1 = tree_to_text({"n1_+": ["n2_*","n3_3"], "n2_*":["n4_2","n5_7"], "n4_2":[],"n5_7":[],"n3_3":[]},"n1_+")
  print(t1)
  t2 = tree_to_text({'n1_+': ['n2_3', 'n3_*'], 'n3_*': ['n4_/', "n5_2"], 'n4_/': ["n6_10", "n7_5"], "n6_10": [], "n7_5": [], "n5_2": [], 'n2_3': []},"n1_+")
  print(t2)
  t3 = tree_to_text({'x_-': ['x1_-', 'x_100'], 'x1_-': ['x_200', 'x_1000'], 'x_100': [], 'x_200': [], 'x_1000': []}, "x_-")
  print(t3)
