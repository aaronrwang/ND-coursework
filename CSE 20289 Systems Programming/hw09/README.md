# Group
| **Name** | **Email** |
| --- | --- |
| Aaron Wang | awang27@nd.edu |
| Derick Shi | dshi2@nd.edu |
| Ethan Little | elittle2@nd.edu |

# Makefile
We edited the Makefile such that doing make would make redextract while doing make redextract-debug would make the debug version with the extra -g flag to enable gdb. Ethan Little mainly worked on this portion of the assignment. 

# Bugs and Fixes
We enabled the SHOW_DEBUG macro in pcap-read by turning it to 1 to see the output. We saw that the fread method calls weren't working in the Packet struct. Adding more print statements, we were able to see that the real issue was that pcap-read.c was calling the allocatePacket method which was returning null. This is due to the fact that there was an if statement that returned null if DEFAULT_READ_BUFFER (Macro of 2500) > PKT_SIZE_LIMIT (Macro of 1500). This could be fixed by lowering the DEFAULT_READ_BUFFER to 1500, increasing the PKT_SIZE_LIMIT to 2500 or by having the program not return null. We decided to decrease the DEFAULT_READ_BUFFER to 1500 because all of the data points seem to not exceed 1500 and in case the PKT_SIZE_LIMIT is important in other areas. Derick Shi mainly worked on this part of the assignment. 

# Task 5
We added the following code to solve the memory leaks. Aaron Wang mainly worked on this part of the assignment.

In main.c line 63, 64
```
free(theInfo.FileName);
free(BigTable);
```

In packet.c line 222
```
discardPacket(pPacket);
```