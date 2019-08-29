class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def cloneLinkedListWithRandomPtr(head):
    '''
    time: O(n)
    space: O(n)
    '''
    if not head:
        return None
    clone_head = Node(None)
    clone = clone_head
    node = head
    while node:
        clone.next = Node(node.val)
        node = node.next
    clone_head = clone_head.next
    clone = clone_head
    node = head
    while node:
        curr = node
        node = node.next
        curr.next = clone
        clone.random = curr
        clone = clone.next
    
    clone = clone_head
    node = head
    while clone:
        clone.random = clone.random.random.next
        node.next = node.next.next.random
        clone = clone.next
        node = node.next
    
    return clone_head