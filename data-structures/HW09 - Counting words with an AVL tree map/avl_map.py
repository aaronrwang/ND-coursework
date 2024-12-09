from avl import Node, AVLTree

class AVLMap(AVLTree):
    # AVLMap is a subclass of AVLTree
    # The constructor calls the constructor of the superclass
    # The constructor takes an optional argument do_balance
    # to enable or disable balancing
    # Input: root (Node) - the root of the AVL tree
    #        do_balance (bool) - whether to balance the tree after insertion or deletion
    # Output: None
    def __init__(self, root=None, do_balance=True):
        super().__init__(root, do_balance)

    # Helper method to insert or update a [key, value] pair
    # It is similar to the insert method in AVLTree, except
    # that it updates the value if the key is already in the tree
    # Input: root (Node) - the root of the AVL tree
    #        key (comparable) - the key to insert or update
    #        value (any) - the value to insert or update
    # Output: Node - the root of the AVL tree
    def _insert_or_update(self, root, key, value):
        if root is None:
            return Node([key,value])
        
        if key == root.key[0]:
            root.key[1] = value
            return root
        
        if key < root.key[0]:
            root.left = self._insert_or_update(root.left, key, value)
        else:
            root.right = self._insert_or_update(root.right, key, value)
        return root
        if self.do_balance:
            # Update the height of the current node
            root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
            # Rebalance the tree
            return self._rebalance(root, [key,value])
        else:
            return root
    
    # Magic method to support assignment using the [] operator
    # Input: key (comparable) - the key to insert or update
    #        value (any) - the value to insert or update
    # Output: None
    def __setitem__(self, key, value):
        self.root = self._insert_or_update(self.root, key, value)

    # Helper method to get the node with the key
    # Used by __getitem__, __contains__, and get
    # Input: root (Node) - the root of the AVL tree
    #        key (comparable) - the key to search for
    # Output: Node - the node with the key, or None if not found
    def _get_node(self, root, key):
        if root is None:
            return None
        if root.key[0] == key:
            return root
        elif key < root.key[0]:
            return self._get_node(root.left, key)
        else: 
            return self._get_node(root.right, key)


    # Magic method to support retrieval using the [] operator
    # Raise a KeyError if the key is not found, consistent with the behavior
    # of the __getitem__ method of the dict class
    # Input: key (comparable) - the key to search for
    # Output: any - the value of the key
    def __getitem__(self, key):
        temp = self._get_node(self.root, key)
        if not temp:
            raise KeyError()
        return temp.key[1]
    
    # Get the value of the key, or return the default value if the key is not found,
    # consistent with the behavior of the get method of the dict class
    # Input: key (comparable) - the key to search for
    #        default (any) - the value to return if the key is not found
    # Output: any - the value of the key
    def get(self, key, default=None):
        temp = self._get_node(self.root, key)
        if not temp:
            return default
        return temp.key[1]


    # Magic method to support the in operator
    # Input: key (comparable) - the key to search for
    # Output: bool - True if the key is in the map, False
    #               otherwise
    def __contains__(self, key):
        temp = self._get_node(self.root, key)
        if not temp:
            return False
        return True

    # Remove a [key, value] pair from the map and return the value,
    # consitent, with the pop method in the dict class 
    # Raise a KeyError if the key is not found
    # Input: key (comparable) - the key to remove
    # Output: any - the value of the key
    def pop(self, key):
        temp = self._get_node(self.root, key)
        if not temp:
            return None
        val = temp.key[1]
        self.remove(temp.key)
        return val
    
    # A generator that yields the [key, value] pairs in the map
    # using an inorder traversal
    # Output: generator - the [key, value] pairs in the map
    def inorder_generator(self):
        yield from self._inorder_generator(self.root)
    
    # Helper recursive generator method that yields the [key, value] pairs 
    # in the map in an inorder traversal
    # Input: root (Node) - the root of the AVL tree
    # Output: generator - the [key, value] pairs in the map
    def _inorder_generator(self, root):
        if root is None:
            return
        if root.left:
            yield from self._inorder_generator(root.left)
        yield root.key
        if root.right:
            yield from self._inorder_generator(root.right)

    # A generator that yields the [key, value] pairs in the map
    # Usage is consistent with the behavior of the items method
    # of the dict class.
    # Hint: You can just yield from the inorder_generator method
    # Output: generator - the [key, value] pairs in the map
    def items(self):
        yield from self.inorder_generator()

    # Magic method to support iteration using a generator
    # This yields the keys only, consistent with
    # the behavior of the iterator for the dict class
    # Output: generator - the keys in the map
    def __iter__(self):
        yield from (x[0] for x in self.inorder_generator())
        
    
