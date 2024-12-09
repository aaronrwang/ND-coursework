# Group
| **Name** | **Email** |
| --- | --- |
| Aaron Wang | awang27@nd.edu |
| Derick Shi | dshi2@nd.edu |
| Ethan Little | elittle2@nd.edu |

# Task 4a
## Unittests
For the unittests, we used data-10.json and just compared the length of each list returned to how many items we expected for simplicity of code. We found the number expected using command-F on the JSON

For stat functions we tested all the stats with the data-10.json and 2 differing filters.

For list, we tested that the generator returned all the values of the list and that it would output "a failure" when the limit of the generator was reached.


**When all data is filtered out, stats will return 0**

**URL = http://ns-mn1.cse.nd.edu/cse20289-fa24/hw03/data-all.json**
**PORT = 40931**

# Task 4b
For the test.sh file an exit command is needed for the script to stop running before the EOF key word. 

# Task 4c
When entering * as a argument for the bb.sh script, it should be placed in quotes for the shell script to receive it properly. Our script was written before the directions were changed for the homeowrk, so it does not require a stat parameter and runs all the stats automatically.

# Task 5
Like with task 4c, our shell script was also written before the change in directions, so it also runs all stats.