CC= gcc
CFLAGS= -Wall -std=gnu99 -g
LD= gcc
LDFLAGS= 

test:
	@$(MAKE) -sk score_all

all: freq unit_hash unit_pair unit_string_utils unit_table

score_all: score_table score_string_utils score_freq

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

unit_hash: unit_hash.o hash.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_pair: unit_pair.o pair.o string_utils.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_table: unit_table.o hash.o pair.o table.o string_utils.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_string_utils: unit_string_utils.o hash.o pair.o table.o string_utils.o
	$(LD) $(LDFLAGS) -o $@ $^

freq: freq.o hash.o pair.o table.o string_utils.o
	$(LD) $(LDFLAGS) -o $@ $^

score_hash: unit_hash
	./score_hash.sh

score_pair: unit_pair
	./score_pair.sh

score_table: unit_table
	./score_table.sh

score_string_utils: unit_string_utils
	./score_string_utils.sh

score_freq: freq
	./score_freq.sh

clean:
	rm -f freq unit_hash unit_pair unit_string_utils unit_table *.a *.o