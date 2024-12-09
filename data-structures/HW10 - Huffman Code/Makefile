test:
	@$(MAKE) -sk test_all

test_all: test_heap test_huffman

test_heap: heap_test.py
	@echo Testing heap ...
	@chmod +x ./heap_test.py
	@./heap_test.py -v
	@echo

test_huffman: huffman_test.py
	@echo Testing huffman ...
	@chmod +x ./huffman_test.py
	@./huffman_test.py -v
	@echo

