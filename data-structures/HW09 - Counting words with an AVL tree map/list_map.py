class ListMap():
    # Constructor
    # The data is a list of [key, value] pairs
    def __init__(self):
        self.data = []
    
    # Helper method to search for the index of the key and its value
    # This function returns two values as a tuple:
    #   the index of the key and the value if found: (index, value)
    #   the index where the key should be inserted and None if not found: (index, None)
    # Note that in a typical binary search, the index where the key should be inserted
    # is the minimum index of the search range when the key is not found
    # Input: key (comparable) - the key to search for
    # Output: tuple - the index of the key and the value if found, 
    #    or the index where the key should be inserted and None if not found
    def _binary_search(self, key):
        if len(self.data) == 0:
            return (0,None)
        l = 0
        r = len(self.data) - 1
        while l <= r:
            m = (l+r)//2
            if self.data[m][0] == key:
                return (m, self.data[m][1])
            elif self.data[m][0] < key:
                l = m + 1
            else:
                r = m - 1
        return (l, None)
    
    # Magic method to support assignment using the [] operator
    # Insert or update the [key, value] pair
    # Uses binary search to locate the index of the key or insertion point
    # Input: key (comparable) - the key to insert or update
    #        value (any) - the value to insert or update
    # Output: None
    def __setitem__(self, key, value):
        temp = self._binary_search(key)
        if temp[1] == None:
            self.data.insert(temp[0], [key,value])
        self.data[temp[0]] = [key, value]
        return None

    # Magic method to support retrieval using the [] operator
    # Raise a KeyError if the key is not found, consistent with the behavior
    # of the __getitem__ method of the dict class
    # Use binary search to locate the index of the key
    # Input: key (comparable) - the key to search for
    # Output: any - the value at the key
    def __getitem__(self, key):
        temp = self._binary_search(key)
        if temp[1] != None:
            return temp[1]
        raise KeyError()
    
    # Get the value of the key, or return the default value if the key is not found,
    # consistent with the behavior of the get method of the dict class
    # Use binary search to locate the index of the key
    # Input: key (comparable) - the key to search for
    #        default (any) - the default value to return if the key is not found
    # Output: any - the value at the key or the default value
    def get(self, key, default=None):
        temp = self._binary_search(key)
        if temp[1] != None:
            return temp[1]
        return default
 
    # Magic method to support the in operator
    # Input: key (comparable) - the key to search for
    # Output: bool - True if the key is found, False otherwise
    def __contains__(self, key):
        temp = self._binary_search(key)
        if temp[1] != None:
            return True
        return False
    
    # Remove a [key, value] pair from the map and return the value,
    # consitent, with the pop method in the dict class 
    # Raise a KeyError if the key is not found
    # Input: key (comparable) - the key to remove
    # Output: any - the value at the key
    def pop(self, key):
        temp = self._binary_search(key)
        if temp[1] != None:
            return self.data.pop(temp[0])[1]
        raise KeyError()
    
    # Magic method to support iteration using a generator
    # Note that this yields the keys only, consistent with
    # the behavior of the iterator for the dict class
    # Output: generator - a generator that yields the keys
    def __iter__(self):
        for item in self.data:
            yield item[0]

    # A generator that yields the [key, value] pairs in the map
    # Usage is consistent with the behavior of the items method
    # of the dict class
    # Output: generator - the [key, value] pairs in the map
    def items(self):
        for item in self.data:
            yield item
    
    

