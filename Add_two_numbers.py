# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.



class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def show(node):
            while node:
                print(node.val, end=', ')
                node = node.next
        curr1= l1
        curr2 = l2
        carry = 0
        head = ListNode(0)
        ptr = head
        end = False
        while not end:
            if curr1 and curr2:
                rem = curr1.val + curr2.val + carry
                #print(rem)
                curr1 = curr1.next
                curr2 = curr2.next     
            elif curr1 and curr2 is None: 
                rem = curr1.val + carry
                curr1 = curr1.next

            elif curr2 and curr1 is None:
                rem = curr2.val + carry
                curr2 = curr2.next
            else:
                break
            carry = rem // 10
            res = rem % 10
            ptr.next = ListNode(res)
            ptr = ptr.next
        if carry > 0:
            ptr.next = ListNode(carry)
            ptr = ptr.next
        show(head.next)
        return head.next

def listToListnode(numbers):
    head = ListNode(0)
    ptr = head
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = head.next
    return ptr


if __name__ == '__main__':
    l1 = listToListnode([2,4,3])
    l2 = listToListnode([5,6,4])
    n = listToListnode([5,5])
    n1 = listToListnode([5])
    Solution().addTwoNumbers(n, n1)
    Solution().addTwoNumbers(l1, l2)