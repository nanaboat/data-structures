# Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.

# Note:

# Given n will always be valid.

# Follow up:

# Could you do this in one pass?

def removeNthFromEnd(head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # This solves the problem after making two passes of the linked list
        # O(n)
        current = head
        size = 0
        while current:
            size += 1
            current = current.next
        idx = size - n
        current = head
        prev = None
        i = 0
        while i != idx:
            prev = current
            current = current.next
            i += 1
        if prev:
            prev.next = current.next
            current.next = None
        else:  # removing the head
            head = current.next
        
        return head