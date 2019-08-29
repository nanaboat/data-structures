from copy import deepcopy
'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

https://leetcode.com/problems/combination-sum-ii/description/
https://leetcode.com/problems/combination-sum/
Time complexity - O(input.size * total_sum)
Space complexity - O(input.size*total_sum)
https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/SubsetSum.java

'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        length = len(candidates)
        def explore(idx, path, t):
            if t == 0:
                res.append(path)
                return
            if t < 0:
                return
            if candidates[idx] > t:
                    return
            #import pdb; pdb.set_trace()
            for i in range(idx, length):
                #p = path + [candidates[i]]
                explore(i, path + [candidates[i]], t - candidates[i])
                #p.pop()
        
        explore(0, [], target)
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        res = []
        length = len(candidates)
        
        def explore(idx, path, t):
            if t == 0:
                res.append(path)
                return
            if t < 0:
                return
            
            for i in range(idx, length):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > t:
                    break
                #p = path + [candidates[i]]
                explore(i+1, path + [candidates[i]], t - candidates[i])
                #p.pop()
        
        explore(0, [], target)
        return res


if __name__ == "__main__":
    print(Solution().combinationSum([2,3,6, 7], 7))