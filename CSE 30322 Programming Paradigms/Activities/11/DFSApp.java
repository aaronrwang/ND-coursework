package Activities.a11;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;

public class DFSApp {
  public static void main(String[] args) {
    // String root = "a";
    // Map<String, List<String>> graph = new HashMap<>();
    // graph.put("a", Arrays.asList("b", "e"));
    // graph.put("b", Arrays.asList("c", "d"));
    // graph.put("c", Arrays.asList("e"));
    // graph.put("d", Arrays.asList("b"));
    // graph.put("e", Arrays.asList("a", "f"));
    // graph.put("f", Arrays.asList());

    // String root = "a";
    // String, List<String>> graph = new HashMap<>();
    // h.put("a", Arrays.asList("b"));
    // h.put("b", Arrays.asList("c", "d"));
    // h.put("c", new ArrayList<>());
    // h.put("d", new ArrayList<>());

    String root = "a";
    Map<String, List<String>> graph = new HashMap<>();
    graph.put("a", Arrays.asList("b"));
    graph.put("b", Arrays.asList("a"));

    DFS dfs = new DFS();
    System.out.println(dfs.traverse(root, graph));

  }
}
