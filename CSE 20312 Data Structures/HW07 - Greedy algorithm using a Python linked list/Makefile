test:
	@$(MAKE) -sk test_all

test_all: test_doubly_linked_list test_priority_queue test_cups

test_doubly_linked_list: doubly_linked_list_test.py
	@echo Testing doubly_linked_list ...
	@chmod +x ./doubly_linked_list_test.py
	@./doubly_linked_list_test.py -v
	@echo

test_priority_queue: priority_queue_test.py
	@echo Testing priority_queue ...
	@chmod +x ./priority_queue_test.py
	@./priority_queue_test.py -v
	@echo

test_cups: cups.py
	@echo Testing Cups...
	@chmod +x ./cups_test.py
	@./cups_test.py -v
	@echo


