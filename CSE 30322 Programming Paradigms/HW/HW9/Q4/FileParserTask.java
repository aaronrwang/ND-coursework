import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;

import java.util.*;

public class FileParserTask implements Runnable {
  File file;
  Map<String, Integer> namesCount;
  Map<String, Integer> occupationsCount;

  // notice that an object of this class is instantiated as shown in the main
  // method
  // (i.e., it receives a File and two Maps in the constructor.
  public FileParserTask(File file, Map<String, Integer> namesCount, Map<String, Integer> occupationsCount) {
    this.file = file;
    this.namesCount = namesCount;
    this.occupationsCount = occupationsCount;
  }

  @Override
  public void run() {
    // schema ID (0), Job Title (1), Email Address (2), FirstName(3), LastName(4)
    // no need to worry about race conditions because we are using atomic methods
    // from Concurrent hashmap.
    String line;
    try (BufferedReader br = new BufferedReader(new FileReader(file))) {
      br.readLine();
      while ((line = br.readLine()) != null) {
        String[] values = line.split(",");

        for (int i = 0; i < values.length; i++) {
          if (i == 1) {
            if (this.occupationsCount.containsKey(values[i])) {
              this.occupationsCount.merge(values[i], 1, Integer::sum);
            } else {
              this.occupationsCount.put(values[i], 1);
            }
          } else if (i == 3) {
            if (this.namesCount.containsKey(values[i])) {
              this.namesCount.merge(values[i], 1, Integer::sum);
            } else {
              this.namesCount.put(values[i], 1);
            }
          }
        }
      }
    } catch (IOException e) {
      e.printStackTrace();
    }
    // System.out.println("run() executed");
  }
}