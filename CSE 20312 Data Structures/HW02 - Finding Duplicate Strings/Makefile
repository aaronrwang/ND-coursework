CC = gcc
CFLAGS=	-Wall -std=gnu99 -g -Iinclude
LD = gcc
LDFLAGS = 

score:		
	@$(MAKE) -sk score_all

score_all: score_string_methods score_string_dups

score_string_methods: unit_string_methods
	./score_string_methods.sh

score_string_dups: string_dups
	./score_string_dups.sh

all: unit_string_methods string_dups

#--------- Do not modify above this line -----------------

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

unit_string_methods: string_methods.o unit_string_methods.o
	$(LD) $(LDFLAGS) -o $@ $^

string_dups: string_methods.o string_dups.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm *.o unit_string_methods string_dups