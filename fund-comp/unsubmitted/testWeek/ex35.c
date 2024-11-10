#include <stdio.h>
#include <string.h>

int main()
{
  char line[20];
  printf("enter a line: ");
  fgets(line, 19, stdin);
//  printf("%s\n", line);

  puts("hello there");
  fputs("hello there", stdout);

  return 0;
}