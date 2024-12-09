CC=	gcc
CFLAGS=	-Wall -std=gnu99 -g
LD=	gcc
LDFLAGS=

score:		
	@$(MAKE) -sk score_all

score_all: score_utilities score_string_array score_string_set score_spellcheck

score_utilities: unit_utilities
	./score_utilities.sh

score_string_array: unit_string_array
	./score_string_array.sh

score_string_set: unit_string_set
	./score_string_set.sh

score_spellcheck: spellcheck
	./score_spellcheck.sh

all: unit_utilities unit_string_array unit_string_set spellcheck

#--------- Do not modify anything above this line -----------------

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

unit_utilities: unit_utilities.o utilities.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_string_array: unit_string_array.o string_array.o utilities.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_string_set: unit_string_set.o string_set.o string_array.o utilities.o
	$(LD) $(LDFLAGS) -o $@ $^

spellcheck: spellcheck.o string_set.o string_array.o utilities.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f unit_utilities unit_string_array unit_string_set spellcheck *.o
