from copy import deepcopy
# https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b
'''
https://medium.com/leetcode-patterns
This problems use the sliding window technique to solve them
https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        table = {}
        for ch in t:
            if ch in table:
                table[ch] += 1
            else:
                table[ch] = 1
        i = 0
        j = 0
        l = 2 ** 32
        count = len(table)
        ans = ""
        #import pdb; pdb.set_trace()
        while j < len(s):
            if s[j] in table:
                table[s[j]] -= 1
                if table[s[j]] == 0:
                    count -= 1
            j += 1
            
            # if count == 0; we have found the substring that contains t.
            # we need to now trim this substring to find the minimum substring that contains t
            while count == 0:
                if j - i < l:
                    l = j -i
                    ans = s[i : j]
                if s[i] in table:
                    table[s[i]] += 1
                    if table[s[i]] > 0:
                        count += 1
                i += 1
        return ans
    
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        t = {}
        word_size = len(words[0])
        window_size = 0
        for word in words:
            if word in t:
                t[word] += 1
            else:
                t[word] = 1
            window_size += len(word)
        if len(s) < window_size:
            return []
        
        result = []
        ref = t
        
        #import pdb; pdb.set_trace()
        # there are only word_size possible starts for a window_size
        # start abd end move in step size = word_size
        for i in range(word_size):
            start = i
            end = i # this points to the end of a window / start of another window.
            t = deepcopy(ref)
            c = len(t)
            while end + word_size <= len(s):
                end_word = s[end : end + word_size]
                if end_word in t:
                    t[end_word] -= 1
                    if t[end_word] == 0:
                        c -= 1
                
                if end + word_size - start == window_size:
                    if c == 0:
                        result.append(start)
                    
                    start_word = s[start : start + word_size]
                    if start_word in t:
                        t[start_word] += 1
                        if t[start_word] > 0:
                            c += 1
                    start += word_size  # slide the window towards end in steps of word_size
                end += word_size # move end to the start of the next word_size
        
        return result
    
    def lengthOfLongestSubstring(self, s):
        '''
        Given a string, find the length of the longest substring without repeating characters.
        Example 1:
        Input: "abcabcbb"
        Output: 3 
        Explanation: The answer is "abc", with the length of 3. 
        '''
        if len(s) <= 1:
            return len(s)
        r = {}
        #res = ""
        ans = 0
        i = 0
        for j in range(len(s)):
            if s[j] in r:
                i = max(r[s[j]], i)
            
            # Uncomment if you are to return longest substring
            #if j -i + 1 > ans:
            #    ans = j - i + 1
            #    res = s[i : j + 1]

            # comment this if you uncomment if clause
            ans = max(ans, j - i + 1)
            r[s[j]] = j + 1
        
        return ans
    
    def lengthOfLongestSubstringKDistinct(self, s, k):
        length = len(s)
        if length <= k:
            return len(s)
        
        m = {}
        i = 0; j = 0; count = 0; l = 0; ans = ""
        while j < length:
            if s[j] in m:
                m[s[j]] += 1
            else:
                m[s[j]] = 1
            
            if m[s[j]] == 1:
                count += 1
            j += 1

            while count > k:
                if m[s[i]] == 1:
                    m[s[i]] -= 1
                    if m[s[i]] == 0:
                        count -= 1
                i += 1
            
            l = max(l, j- i)
        
        return l

if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    #words = ["bar","foo","the"]
    print(Solution().findSubstring(s, words))
    print(Solution().minWindow("a", "a"))
    print(Solution().lengthOfLongestSubstring('abcabcbb'))