class Node:
    # Constructor for a node with data
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # Constructor for an empty list
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        # Used for __iter__ which supports the syntax:  for data in dll:
        self.iter_state = None
    
    # Insert a new node after the given node
    # This is a private method and should not be called directly from outside the class
    def _insert_after(self, node, data):
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node
        node.next.prev = new_node
        node.next = new_node
        self.size += 1
    
    # Remove the given node and return its data
    # This is a private method and should not be called directly from outside the class
    def _pop_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        return node.data
    
    # Insert after the last node
    def append(self, data):
        self._insert_after(self.tail.prev, data)
  
    # Insert before the node at the given index
    def insert(self, index, data):
        if index < 0:
            index = -index
            node = self.tail
            while index > 0 and node != self.head:
                node = node.prev
                index -= 1
            if node == self.head:
                raise IndexError
            self._insert_after(node.prev, data)
        else:
            node = self.head
            while index > 0 and node != self.tail.prev:
                node = node.next
                index -= 1
            if node == self.tail.prev:
                raise IndexError
            self._insert_after(node, data)

    # Add a new node in order after the last node with data less than the given data
    def insert_ordered(self, data):
        # TODO
        curr = self.head.next
        while curr != self.tail:
            if curr.data > data:
                self._insert_after(curr.prev,data)
                return
            curr=curr.next
        self.append(data)



    # Remove and return the data of the node at the given index
    # Negative indices count from the end of the list
    def pop(self, index):
        # TODO
        if abs(index) >= self.size:
            raise IndexError
        if index >= 0:
            if index >= self.size:
                raise IndexError
            node = self.head.next
            for _ in range(index):
                node = node.next
            return self._pop_node(node)  
        else:
            index = abs(index)-1
            if index >= self.size:
                raise IndexError
            node = self.tail.prev
            for _ in range(index):
                node = node.prev
            return self._pop_node(node)  


    # Remove all nodes except head and tail
    def clear(self):
        # TODO:
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    # Return the index of the first node with the given data
    def index(self, data):
        index = 0
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return index
            index += 1
            node = node.next
        return -1

    # Sort the list in ascending order using insertion sort
    def sort(self):
        # TODO
        if self.size <= 1:
            return
        curr = self.head
        while curr.next != self.tail:
            temp = curr.next
            src = temp
            while src != self.tail:
                if src.data < temp.data:
                    temp = src
                src=src.next
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.next = curr.next
            temp.prev = curr
            curr.next = temp
            temp.next.prev = temp
            curr = curr.next

    
    # Return a string representation of the list
    # Supports the following syntax to convert a list to a string:  str(dll)
    def __str__(self):
        lst = []
        node = self.head.next
        while node != self.tail:
            lst.append(str(node.data))
            node = node.next
        return ' '.join(lst)

    # Return True if the list is not empty
    # Supports the if dll: syntax to check if the list is not empty
    def __bool__(self):
        return self.head.next != self.tail
    
    # Return True if the list contains a node with the given data
    # Supports the syntax:  data in dll
    def __contains__(self, data):
        node = self.head.next
        while node != self.tail:
            if node.data == data:
                return True
            node = node.next
        return False

    # Return the number of nodes in the list
    # Supports the syntax:  len(dll)
    def __len__(self):
        return self.size

    # Return the data of the node at the given index
    # Supports the syntax:  data = dll[index]
    # Negative indices count from the end of the list
    def __getitem__(self, index):
        # TODO
        if index >= 0:
            if index >= self.size:
                raise IndexError
            node = self.head.next
            for _ in range(index):
                node = node.next
            return node.data 
        else:
            index = abs(index)-1 
            if index > self.size:
                raise IndexError
            node = self.tail.prev
            for _ in range(index):
                node = node.prev
            return node.data

    # Set the data of the node at the given index
    # Supports the syntax:  dll[index] = data
    # Negative indices count from the end of the list
    def __setitem__(self, index, data): 
        # TODO
        if index >= 0:
            if index >= self.size:
                raise IndexError
            node = self.head.next
            for _ in range(index):
                node = node.next
            node.data = data
        else:
            index = abs(index)-1 
            if index > self.size:
                raise IndexError
            node = self.tail.prev
            for _ in range(index):
                node = node.prev
            node.data = data
    
    # Initialize the iterator state
    # Supports the syntax:  for data in dll:
    def __iter__(self):
        self.iter_state = self.head.next
        return self
    
    # Return the next data from the iterator
    # Supports the syntax:  for data in dll:
    def __next__(self):
        if self.iter_state == self.tail:
            raise StopIteration
        data = self.iter_state.data
        self.iter_state = self.iter_state.next
        return data
    
    
        


