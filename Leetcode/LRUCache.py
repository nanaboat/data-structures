from collections import deque
from LRUDoubleLInkedList import LRUDoubleLinkedList, LRUNode

class LRUCache:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.node_map = {}
        self.node_list = LRUDoubleLinkedList()
    
    def get(self, key):
        node = self.node_map.get(key)
        if node:
            self.node_list.remove_node(node)
            self.node_list.add_to_top(node)
            return node.data

        return node
    
    def add(self, key, value):
        node = self.node_map.get(key)
        # node exists; update node value
        if node:
            node.data = value
            self.node_list.remove_node(node)
            self.node_list.add_to_top(node)
        else:
            # if cache is full; remove least recently used node
            if self.size == self.capacity:
                del_node = self.node_list.remove_last_node()
                del(self.node_map[del_node.key])
                self.size -= 1
            else:
                node = LRUNode(key, value)
                self.node_map[key] = node
                self.node_list.add_to_top(node)
                self.size += 1