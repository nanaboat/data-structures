class LRUNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.previous = None
    


class LRUDoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.tail.previous = self.head
    
    def add_to_top(self, node):
        node.next = self.head.next
        self.head.next.previous = node
        node.previous = self.head
        self.head.next = node
    
    def remove_node(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous
        node.next = None
        node.previous = None
    
    def remove_tail_node(self):
        node = self.tail.previous
        self.remove_node(node)
        return node