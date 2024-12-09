# Compiler and flags
CC = gcc
CFLAGS = -Wall --std=c99 -lpthread -lm      # Basic flags for production build
DEBUG_FLAGS = -g                             # Debugging flags
OBJS = packet.o pcap-read.o pcap-process.o main.o  # List of object files

# Default target: build the regular executable
all: redextract


redextract: $(OBJS)
	$(CC) $(OBJS) -o redextract

# Debug redextract-debug executable (with debugging symbols)
redextract-debug: $(OBJS)
	$(CC) $(CFLAGS) $(DEBUG_FLAGS) $(OBJS) -o redextract-debug


packet.o: packet.c packet.h
	$(CC) $(CFLAGS) -c packet.c

pcap-read.o: pcap-read.c pcap-read.h packet.h
	$(CC) $(CFLAGS) -c pcap-read.c

pcap-process.o: pcap-process.c pcap-process.h packet.h
	$(CC) $(CFLAGS) -c pcap-process.c

main.o: main.c packet.h pcap-read.h pcap-process.h
	$(CC) $(CFLAGS) -c main.c

# Clean up object files and the executables
clean: 
	rm -f *.o redextract redextract-debug

