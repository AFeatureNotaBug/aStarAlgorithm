#Priority queue based on Node fCost for use in A* algorithm

class pQueue():
    class Node():
        def __init__(self, node):
            self.next = None
            self.prev = None
            self.node = node
            
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    #Return highest priority node in queue
    def get(self):
        if self.head:
            retNode = self.head
            self.head = self.head.next
        
            return retNode.node
            
        else:
            return None
    
    
    #Insert new node into queue
    def insert(self, node):
        newNode = self.Node(node)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            
            return 1
        
        else:
            current = self.head
            
            while (current is not None and node.fCost > current.node.fCost):
                current = current.next
            
            if current is None:
                self.tail = newNode
            
            elif current == self.head:
                self.head = newNode
                newNode.next = current
                current.prev = newNode
                
            else:
                current.prev.next = newNode
                
                newNode.prev = current.prev
                newNode.next = current
                
                current.prev = newNode
    
    
    #Clear queue
    def clear(self):
        self.head = None
        self.tail = None
