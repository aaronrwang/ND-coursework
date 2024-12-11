import doubly_linked_list as dll

class PriorityQueue:
    def __init__(self, data=None):
        self.dll = dll.DoublyLinkedList()
        # TODO
        if data is not None:
            for item in sorted(data):
                self.dll.append(item)
        

    def push(self, data):
        # TODO
        self.dll.insert_ordered(data)
    
    def pop(self):
        # TODO
        if self.__bool__:
            return self.dll._pop_node(self.dll.tail.prev)
    
    def peek(self):
        # TODO
        if self.__bool__:
            return self.dll.tail.prev.data
    
    def __str__(self):
        # TODO
        lst = []
        node = self.dll.head.next
        while node != self.dll.tail:
            lst.append(str(node.data))
            node = node.next
        return ' '.join(lst)
    
    def __bool__(self):
        # TODO
        return True if self.__len__() > 0 else False
    
    def __len__(self):
        # TODO
        return self.dll.size

