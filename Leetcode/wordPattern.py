class Solution:
    def wordPattern(self, pattern, str):
        if not pattern:
            return len(str) == 0
        word = str.split(' ')
        if len(pattern) != len(word):
            return False
        w_map = {}
        for i in range(len(word)):
            if pattern[i] not in w_map and word[i] not in w_map.values():
                w_map[pattern[i]] = word[i]
            elif w_map.get(pattern[i]) != word[i]:
                return False
        return True
    
    '''
    Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a
    letter in pattern and a non-empty substring in str.

    Examples:
    pattern = "abab", str = "redblueredblue" should return true.
    pattern = "aaaa", str = "asdasdasdasd" should return true.
    pattern = "aabb", str = "xyzabcxzyabc" should return false.
    '''
    def wordPattern2(self, pattern, astr):
        if not pattern:
            return len(astr) == 0
        
        word_map = {}
        str_set = set()
        #return self.isValidPattern(pattern, astr, 0, 0 , word_map, str_set)
        return self.check(pattern, astr, word_map)
    
    def isValidPattern(self, pattern, astr, i, j, w_map, s_set):
        if i == len(pattern) and j == len(astr):
            return True
        if i >= len(pattern) or j >= len(astr):
            return False
        
        char = pattern[i]

        for k in range((j+1), len(astr)):
            sub_str = astr[j : k]
            if char not in w_map and sub_str not in s_set:
                w_map[char] = sub_str
                s_set.add(sub_str)
                if self.isValidPattern(pattern, astr, i + 1, k, w_map, s_set):
                    return True
                print(w_map)
                del(w_map[char])
                print(w_map)
                s_set.remove(sub_str)
            elif char in w_map and w_map[char] == sub_str:
                if self.isValidPattern(pattern, astr, i + 1, k, w_map, s_set):
                    return True
        return False
    
    def check(self, pattern, text, w_map):
        print(w_map)
        if len(pattern) == 0 and len(text) == 0:
            return True

        if len(text) == 0 or len(pattern) == 0:
            return False
        
        if pattern[0] in w_map:
            tmp = w_map[pattern[0]]

            if len(tmp) > len(text) or text[:len(tmp)] != tmp:
                return False
            else:
                return self.check(pattern[1:], text[len(tmp):], w_map)
        else:
            for i in range(1, len(text)):
                w_map[pattern[0]] = text[:i]
                if self.check(pattern[1:], text[i:], w_map):
                    return True
                del w_map[pattern[0]]

        return False

if __name__ == "__main__":
    pattern = "abab" 
    astr = "redblueredblue"
    pattern1 = "aabb"
    astr1 = "xyzabcxzyabc"
    print(Solution().wordPattern2(pattern1, astr1))