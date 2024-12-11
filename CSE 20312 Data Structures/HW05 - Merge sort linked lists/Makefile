score:		
	@$(MAKE) -sk score_all

score_all: score_list score_merge_sort

score_list:	unit_list
	./score_list.sh

score_merge_sort: merge_sort
	./score_merge_sort.sh

all: unit_list merge_sort

#--------- Do not modify anything above this line! -----------------

%.o: %.c
	gcc -c -g -Wall -o $@ $^

unit_list: unit_list.o list.o
	gcc -o $@ $^

merge_sort: merge_sort.o list.o
	gcc -o $@ $^

clean:
	rm -f *.o unit_list merge_sort