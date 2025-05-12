package Activities.a11;

import java.util.*; // imports all classes from java.util package

public class DFS {

  public List<String> traverse(String root, Map<String, List<String>> graph) {
    // queue with nodes to be visited
    Stack<String> toVisit = new Stack<String>();
    toVisit.push(root); // initializes queue with root node
    // list of visited nodes
    List<String> output = new ArrayList<>();
    // set of visited nodes, to avoid getting stuck
    Set<String> visited = new HashSet<>();
    // keep visiting while there are nodes in the queue
    while (!toVisit.isEmpty()) {
      String node = toVisit.pop(); // front of the queue
      if (!visited.contains(node)) { // node wasn't visited yet
        output.add(node); // adds to the output
        visited.add(node); // mark as visited
        Collections.reverse(graph.get(node));
        toVisit.addAll(graph.get(node)); // adds all children to the queue
        Collections.reverse(graph.get(node));
      }
    }
    return output; // returns the visited nodes, in order
  }
}
