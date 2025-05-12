`
[graph.js] Create an object named graph in JavaScript that represents a simple undirected graph using an adjacency list. Your object should:
Provide a method addNode(n) to add a new node to the graph. 
Provide a method addEdge(n1, n2) to add an edge between two nodes in the graph.
Provide methods for Breadth-First Search (bfs(startNode)) and Depth-First Search (dfs(startNode)). 
As of now, you can leave the implementation for the methods listed in #1 - #3 empty (we will see in class how to implement those). The goal of this activity is for you to practice creating objects in JS. 
`

function addNode(n) {
  this.adjacency_list[n] = []
}
function addEdge(a, b) {
  this.adjacency_list[a].push(b)
  this.adjacency_list[b].push(a)
}
function dfs() {
  let stack = []
  let visited = new Set()
  let results = []
  stack.push(startNode);

  while (stack.length != 0) {
    let current = stack.pop();
    if (!visited.has(current)) {
      results.push(current);
      visited.add(current);
      let children = this.adjacencyList.get(current);
      for (let i = children.length - 1; i >= 0; i--) {
        stack.push(children[i])
      }
    }
  }
  return results;
}
function bfs() {
  let queue = []
  let visited = new Set()
  let results = []
  queue.push(startNode);

  while (queue.length != 0) {
    let current = queue.shift();
    if (!visited.has(current)) {
      results.push(current);
      visited.add(current);
      let children = this.adjacencyList.get(current);
      for (let i = children.length - 1; i >= 0; i--) {
        queue.push(children[i])
      }
    }
  }
  return results;

}

const graph = {
  adjacency_list: new Map(),
  addNode: addNode,
  addEdge: addEdge,
  dfs: dfs,
  bfs: bfs
}
graph.addNode(1)
graph.addNode(2)
graph.addEdge(1, 2)
console.log(graph)

