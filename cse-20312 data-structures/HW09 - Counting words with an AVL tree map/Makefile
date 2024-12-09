test:
	@$(MAKE) -sk test_all

test_all: test_avl_map test_list_map test_word_count

test_avl_map: avl_map_test.py
	@echo Testing avl_map ...
	@chmod +x ./avl_map_test.py
	@./avl_map_test.py -v
	@echo

test_list_map: list_map_test.py
	@echo Testing list_map ...
	@chmod +x ./list_map_test.py
	@./list_map_test.py -v
	@echo

test_word_count: word_count_test.py
	@echo Testing word_count ...
	@chmod +x ./word_count_test.py
	@./word_count_test.py -v
	@echo
