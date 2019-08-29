'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
https://leetcode.com/problems/happy-number/discuss/56913/Beat-90-Fast-Easy-Understand-Java-Solution-with-Brief-Explanation

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        h_set = set()
        while n not in h_set:
            h_set.add(n)
            sq_sum = 0
            while n > 0:
                r = n % 10
                sq_sum += (r * r)
                n //= 10
            if sq_sum == 1:
                return True
            else:
                n = sq_sum
            
        return False
    
    def reverseBits(self, n):
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res