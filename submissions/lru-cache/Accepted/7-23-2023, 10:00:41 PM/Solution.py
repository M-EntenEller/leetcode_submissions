// https://leetcode.com/problems/lru-cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "key-{} value-{}".format(self.key, self.value)

class LRUCache:

    def __init__(self, capacity: int):
        self._hashmap = {}
        self.capacity = capacity
        self.n = 0
        self.head = None
        self.tail = None

    def is_full(self):
        return self.n == self.capacity

    def touch_node(self, node):
        if node == self.head:
            return

        node.prev.next = node.next
        if not node == self.tail:
            node.next.prev = node.prev
        else: 
            self.tail = self.tail.prev
            
        self.head.prev = node
        node.next = self.head
        self.head = node

    def get(self, key: int) -> int:
        node = self._hashmap.get(key, None)
        if node: 
            self.touch_node(node)
            return node.value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:     
        node = self._hashmap.get(key, None)
        if node:
            node.value = value
            self.touch_node(node)
            return

        new_node = Node(key, value)

        if self.is_full():
            
            self._hashmap.pop(self.tail.key) 
            self._hashmap[key] = new_node

            if self.capacity > 1:   
                
                self.tail.prev.next = None 
                self.tail = self.tail.prev
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                self.head = self.tail = new_node

            return

        self._hashmap[key] = new_node
        self.n += 1

        if not (self.head and self.tail):
            self.head = self.tail = new_node
            return 

        if self.head: 
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return 

        
        
       


        

        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)