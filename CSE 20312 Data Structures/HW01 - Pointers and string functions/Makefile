score:
	@$(MAKE) -sk score_all

score_all: score_unit_string_functions

score_unit_string_functions: unit_string_functions
	./score_unit_string_functions.sh

all: unit_string_functions

#--------- Do not modify above this line -----------------

string_functions.o: string_functions.c string_functions.h
	gcc -Wall -g -c string_functions.c

unit_string_functions.o: unit_string_functions.c string_functions.h
	gcc -Wall -g -c unit_string_functions.c

unit_string_functions: unit_string_functions.o string_functions.o
	gcc -o unit_string_functions unit_string_functions.o string_functions.o

clean:
	rm *.o unit_string_functions