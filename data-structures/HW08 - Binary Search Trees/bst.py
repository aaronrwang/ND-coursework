from tree_print import pretty_tree

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

class BSTree:
    # Constructor
    # Optionally, you can initialize the tree with a root node
    def __init__(self, root=None):
        self.root = root
    
    # Clear the tree
    def clear(self):
        self.root = None

    # Insert a Node with a given key into the tree
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Helper function for insert
    def _insert(self, root, key):
        if root is None:
            return Node(key)
        
        if key == root.key:
            return root
        
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    # Magic method: check if the tree contains a key
    # Support for the 'in' operator
    def __contains__(self, key):
        return self._search(self.root, key) is not None
    
    # Helper function for contains
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)  
    
    # Inorder traversal
    def inorder(self):
        return self._inorder(self.root)

    # Helper function for inorder
    def _inorder(self, root):
        if not root:
            return []

        return (
            self._inorder(root.left) + 
            [root.key] + 
            self._inorder(root.right))
    
    # Magic method: et the length of the tree 
    # Suport for the len() function 
    def __len__(self):
        return self._len(self.root)
    
    # Helper function for len
    def _len(self, root):
        if not root:
            return 0
        
        left_len = self._len(root.left)
        right_len = self._len(root.right)

        return 1 + left_len + right_len
    
    # Get the height of the tree
    def height(self):
        return self._height(self.root)
    
    # Helper function for height
    def _height(self, root):
        if root == None:
            return -1
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return 1 + max(left_height, right_height)

    # Remove a Node with a given key from the tree  
    def remove(self, key):
        self.root = self._remove(self.root, key)
    
    # Helper function for remove
    def _remove(self, root, key):
        if root is None:
            return root
        
        # Key is not yet found
        if key < root.key:
            root.left = self._remove(root.left, key)
        elif key > root.key:
            root.right = self._remove(root.right, key)

        # Key is found
        else:
            # Node with only one child or leaf node: return the non-null child
            # If the node has no children, return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.key = self._min_value_node(root.right)
            # Delete the inorder successor
            root.right = self._remove(root.right, root.key)
        return root
    
    # Helper function to find the minimum value node in a tree
    def _min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.key

    # Write the BFS traversal of the tree to a list
    def write_bfs(self):
        # If the tree is empty, return an empty list
        if self.root is None:
            return []
        
        # Push the root node to the queue
        queue = [self.root]

        # List to store the BFS traversal results
        bfs = []

        # While there are nodes to process
        while queue:
            # Pop the first node from the queue
            node = queue.pop(0)

            # If the node is None (missing children), append None to the BFS list
            if node is None:
                bfs.append(None)
            
            # If the node is not None, append its key to the results and push its children to the queue
            else:
                bfs.append(node.key)
                queue.append(node.left)
                queue.append(node.right)
        
        # Remove trailing None values
        while bfs and bfs[-1] is None:
            bfs.pop()
        
        # Return the BFS traversal list
        return bfs
    
    # Magic method: string representation of the tree
    # Support for the print() function
    def __str__(self):
        return pretty_tree(self)
    
    # ---- Homework methods ----

    # Preorder traversal
    def preorder(self):
        return self._preorder(self.root)

    # Helper function for preorder
    def _preorder(self, root):
        if not root:
            return []
        return [root.key] + self._preorder(root.left) + self._preorder(root.right)
    
    # Postorder traversal
    def postorder(self):
        return self._postorder(self.root)

    # Helper function for postorder
    def _postorder(self, root):
        if not root:
            return []
        return self._postorder(root.left) + self._postorder(root.right) + [root.key]
    
    # Check if the tree is balanced
    def is_balanced(self):
        return self._is_balanced(self.root)[0]
    
    # Helper function for is_balanced
    def _is_balanced(self, root):
        if not root:
            return [True,0]
        l = self._is_balanced(root.left)
        r = self._is_balanced(root.right)
        return [(l[1] == r[1] or l[1]+1 == r[1] or l[1] == r[1]+1) and l[0] and r[0] , max(l[1],r[1])+1] 

    
    # Invert the tree
    def invert(self):
        self.root = self._invert(self.root)
    
    # Helper function for invert
    def _invert(self, root):
        if not root:
            return root
        self._invert(root.left)
        self._invert(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root
    
    # Get all paths from root to leaves
    def paths(self):
        return self._paths(self.root)

    # Helper function for paths
    def _paths(self, root, path=[]):
        if not root:
            return []
        path = path +[root.key]
        l,r=[],[]
        if root.left:
            l = self._paths(root.left, path)
        if root.right:
            r = self._paths(root.right, path)
        if not root.left and not root.right:
            return [path]
        return l+r
        
    
    # Read a list in BFS order and construct the tree
    def read_bfs(self, lst):
        if not lst:
            return
        self.root = Node(lst[0])
        queue = [self.root]
        n = len(lst)
        i = 1
        while i < n:
            temp = queue.pop(0)
            if lst[i]:
                temp.left = Node(lst[i])
                queue.append(temp.left)
            i+=1
            if i == n:
                break
            if lst[i]:
                temp.right = Node(lst[i])
                queue.append(temp.right)
            i+=1
        queue = [self.root]

    # Check if the tree is a valid BST
    def is_valid_bst(self):
        return self._is_valid_bst(self.root)
        
    def _is_valid_bst(self, root, minn=None, maxx=None):
        if not root:
            return True
        l, r = True, True
        if root.left:
            if root.left.key >= root.key or (minn and root.left.key <= minn):
                l =  False
            else:
                l = self._is_valid_bst(root.left,minn,root.key)
        if root.right:
            if root.right.key <= root.key or (maxx and root.right.key >= maxx):
                r = False
            else:
                r = self._is_valid_bst(root.right,root.key,maxx)
        return l and r

    


    

    
            


