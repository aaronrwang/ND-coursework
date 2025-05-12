from collections import deque 

def bfs_traversal(graph, initial_node):
  # your implementation here
  # your function will return a list!

  # bfs traversal code
  q = deque([initial_node])
  visited = [] # this is the list that is returned
  visited_set = set([]) # used to check if smth has been visited already
  while q:
    node = q.popleft() # get first element of queue
    if node in visited_set: # if already visited move on
      continue
    visited.append(node) # add to list
    visited_set.add(node) # add to set
    for next_node in graph[node]: # add all children to queue
      q.append(next_node)
  return visited

if __name__ == "__main__":
  print(bfs_traversal({"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]},"+"))
  print(bfs_traversal({0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]},0))
