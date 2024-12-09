test:
	@$(MAKE) -sk test_all

test_all: test_bst

test_bst: bst_test.py
	@echo Testing bst ...
	@chmod +x ./bst_test.py
	@./bst_test.py -v
	@echo
