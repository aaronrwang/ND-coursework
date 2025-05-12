import java.util.*;

public class TreeTraversal {
  public static void main(String[] args) {

    // Test case 1
    String root = "a";
    Map<String, List<String>> tree = new HashMap<>();
    tree.put("a", Arrays.asList("b", "c"));
    tree.put("b", Arrays.asList());
    tree.put("c", Arrays.asList("d", "e"));
    tree.put("d", Arrays.asList());
    tree.put("e", Arrays.asList());

    // Test case 2
    // String root = "A";
    // Map<String, List<String>> tree = new HashMap<>();
    // tree.put("A", Arrays.asList("B", "C"));
    // tree.put("B", Arrays.asList("D", "E"));
    // tree.put("C", Arrays.asList("F", "G"));
    // tree.put("D", Arrays.asList());
    // tree.put("E", Arrays.asList());
    // tree.put("F", Arrays.asList());
    // tree.put("G", Arrays.asList());

    // Print test case output
    TreeTraversal t = new TreeTraversal();
    System.out.println(t.traverse(root, tree));
  }

  public List<String> traverse(String root, Map<String, List<String>> tree) {
    Deque<String> toVisit = new LinkedList<>();
    toVisit.add(root);
    List<String> output = new ArrayList<>();
    Set<String> visited = new HashSet<>();
    visited.add(root);
    int counter = 0;
    while (!toVisit.isEmpty()) {
      Deque<String> newToVisit = new LinkedList<>();
      List<String> newOutput = new ArrayList<>();
      while (!toVisit.isEmpty()) {
        String node;
        node = toVisit.removeFirst();
        newOutput.add(node);
        for (String neighbor : tree.get(node)) {
          if (!visited.contains(neighbor)) {
            visited.add(neighbor);
            newToVisit.addLast(neighbor);
          }
        }

      }
      counter += 1;
      toVisit = newToVisit;
      if (counter % 2 == 1) {
        Collections.reverse(newOutput);
      }
      output.addAll(newOutput); // modifies list1 directly
    }

    return output;
  }
}
