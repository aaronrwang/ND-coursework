CC=	gcc
CFLAGS=	-Wall -std=gnu99 -g
LD=	gcc
LDFLAGS=

score:		
	@$(MAKE) -sk score_all

score_all: score_array score_stack score_set score_rpn score_palindromic

score_array: unit_array
	./score_array.sh

score_stack: unit_stack
	./score_stack.sh

score_set: unit_set
	./score_set.sh

score_rpn: rpn
	./score_rpn.sh

score_palindromic: palindromic
	./score_palindromic.sh

all: unit_array unit_stack unit_set rpn palindromic

#--------- Do not modify anything above this line -----------------

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

unit_array:	unit_array.o array.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_stack:	unit_stack.o array.o stack.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_set: unit_set.o array.o set.o
	$(LD) $(LDFLAGS) -o $@ $^

rpn: rpn.o array.o stack.o
	$(LD) $(LDFLAGS) -o $@ $^ 

palindromic: palindromic.o array.o set.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f rpn palindromic unit_array unit_stack unit_set *.o
