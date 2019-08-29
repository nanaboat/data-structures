# Problem 1: Power Set
#
# Prompt:   Given a set S, return the powerset P(S), which is
#           a set of all subsets of S.
#
# Input:    A String
# Output:   An Array of String representing the power set of the input
#
# Example:  S = "abc", P(S) = ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
#
# Note:     The input string will not contain duplicate characters
#           The letters in the subset string must be in the same order
#           as the original input.
"""
https://www.youtube.com/watch?v=3dEVYiyFKac
https://www.geeksforgeeks.org/recursive-program-to-generate-power-set/
https://www.geeksforgeeks.org/power-set/
Assumptions:
- no leading or trailing spaces
- no wilcard characters 
- all alphabets 


"antho"
- ["", a, n,t, h, o, an, at,ah,ao, nt, nh, no, th, to, ho, .....]


      .
 S = "abc", P(S) = ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

          
         " "
        /    \
   



1. recursion function parameters
2. Invoke the function
3. Identify base case
4. identify recursion case

Perform opertation @ each character
  - add nothing to it
  - add the next character to it



 S = "abc", 
 P(S) = ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']

results = [""]


                        " "                           - 0
                    /              \
                    ""              "a"              - 1
                  
                /     \          /       \
                  
              ""       b        "a"    "ab"            - 2    
 
            / \ . .   / \ . . /   \      /   \
          ""  "c"  "b" "bc"  "a"  "ac"  "ab" "abc" . .  - 3


helper(substring, depth, results)
 base case : 
  if depth >= len(input string)
    append(substring) to results
    return

  helper(substring, depth + 1, results)
  helper(substring + input[depth], depth + 1, results)

  Time complexity: O(n* 2**n)   For every i in set there are two recursive calls made (with substring or without substring)
  Space complexity: O(n* 2**n)
  
"""
class RecPowerSet:
    '''Recursive solution.'''
    def powerSet(self, astr):
        result = []
        self.generatePowerSet("", astr, 0, result)
        return result
    
    def generatePowerSet(self, sub_string, astr, index, result):
        if index == len(astr):
            result.append(sub_string)
        else:
            self.generatePowerSet(sub_string, astr, index + 1, result)
            self.generatePowerSet(sub_string + astr[index], astr, index + 1, result)
    
    def getSubsets(self, astr):
        results = []
        self.get_subsets([''], astr, 0, results)
        return results
    
    def get_subsets(self, sub, astr, idx, res):
        if idx == len(astr):
            res.append(''.join(sub))
        else:
            self.get_subsets(sub, astr, idx + 1, res)
            self.get_subsets(sub + [astr[idx]], astr, idx + 1, res)

    def getPowerSet(self, astr):
        ''' Iterative solution.'''
        size = 2 ** len(astr)
        result = []
        for i in range(size):
            temp = []
            for j in range(len(astr)):
                if (i & (1 << j) > 0):
                    temp.append(astr[j])
            result.append(''.join(temp))
        return result
    
    def subsets(self, astr):
        result = []
        self.backtrack('', astr, result)
        return result

    def backtrack(self, sub, astr, result):
        if astr == "":
            result.append(sub)
        else:
            self.backtrack(sub + astr[0], astr[1:], result)
            self.backtrack(sub, astr[1:], result)
    
    def powerset(self, nums):
        result = []
        self._backtrack('', nums, 0, result)
        return result
    
    def _backtrack(self, sub, astr, start, result):
        result.append(sub)

        for i in range(start, len(astr)):
            s = [sub + astr[i]]
            self._backtrack(s[0], astr, i+1, result)
            # remove astr[i] from s and explore further subsets
            #s.pop()

    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

        Note: The solution set must not contain duplicate subsets.
        """
        def getPowersets(sub, idx, res):
            if idx == len(nums):
                res.append(sub)
            
            else:
                if len(sub) > 0 and sub[-1] == nums[idx]:
                    getPowersets(sub + [nums[idx]], idx +  1, res)
                else:
                    getPowersets(sub + [nums[idx]], idx + 1, res)
                    getPowersets(sub, idx + 1, res)
        
        res = []
        nums.sort()
        getPowersets([], 0, res)
        return res
    
    def powersetWithDup(self, nums):

        def getPowerSet(sub, start, res):
            res.append(sub)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                #s = sub + [nums[i]]
                getPowerSet(sub + [nums[i]], i + 1, res)
                #s.pop()
        
        nums.sort()
        res = []
        getPowerSet([], 0 , res)
        return res

if __name__ == "__main__":
    print(RecPowerSet().getSubsets(['a', 'b', 'c']))
    print('=========================\n===============================')
    print(RecPowerSet().getPowerSet('abc'))
    print(RecPowerSet().powersetWithDup([4,4,4,1]))
    

