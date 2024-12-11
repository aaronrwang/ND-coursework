CMP = gcc
MAIN = crossword
FUNC = func
EXEC = runcrossword

$(EXEC): $(FUNC).o $(MAIN).o 
	$(CMP) $(FUNC).o $(MAIN).o -Wall -lm -o $(EXEC)

$(FUNC).o: $(FUNC).c $(FUNC).h 
	$(CMP) -c $(FUNC).c -Wall -o $(FUNC).o 

$(MAIN).o: $(MAIN).c $(FUNC).h
	$(CMP) -c $(MAIN).c -Wall -o $(MAIN).o 

clean:
	rm *.o
	rm $(EXEC)

