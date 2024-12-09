class MaxHeap:
    def __init__(self):
        self.heap_array = []
        
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2
            
            # check for a violation of the max heap property
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                # print("   percolate_up() swap: %d <-> %d" % (self.heap_array[parent_index], self.heap_array[node_index]))
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                # continue the loop from the parent node
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the max among the node and all the node's children
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i = i + 1

            # check for a violation of the max heap property
            if max_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                # print("   percolate_down() swap: %d <-> %d" % (self.heap_array[node_index], self.heap_array[max_index]))
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = temp
                
                # continue loop from the max index node
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        # add the new value to the end of the array.
        # print("insert(%d):" % value)
        self.heap_array.append(value)
        
        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)
        
    def remove(self):
        # save the max value from the root of the heap.
        # print("remove():")
        max_value = self.heap_array[0]
        
        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            
            # percolate down to restore max heap property.
            self.percolate_down(0)
                
        # return the max value
        return max_value
    
    def __len__(self):
        return len(self.heap_array)
      
class MinHeap:
    def __init__(self):
        self.heap_array = []
        
    def percolate_up(self, node_index):
        while node_index > 0:
            # compute the parent node's index
            parent_index = (node_index - 1) // 2
            
            # check for a violation of the max heap property
            if self.heap_array[node_index] >= self.heap_array[parent_index]:
                # no violation, so percolate up is done.
                return
            else:
                # swap heap_array[node_index] and heap_array[parent_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                
                # continue the loop from the parent node
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]

        while child_index < len(self.heap_array):
            # Find the max among the node and the node's children
            min_value = value
            min_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] < min_value:
                    min_value = self.heap_array[i + child_index]
                    min_index = i + child_index
                i = i + 1

            # check for a violation of the max heap property
            if min_value == value:
                return
            else:
                # swap heap_array[node_index] and heap_array[max_index]
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[min_index]
                self.heap_array[min_index] = temp
                
                # continue loop from the larger child node
                node_index = min_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        # add the new value to the end of the array.
        self.heap_array.append(value)
        
        # percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)
        
    def remove(self):
        # save the max value from the root of the heap.
        max_value = self.heap_array[0]
        
        # move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            
            # percolate down to restore max heap property.
            self.percolate_down(0)
                
        # return the max value
        return max_value
    
    def __len__(self):
        return len(self.heap_array)
        