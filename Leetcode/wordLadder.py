'''
127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        '''
        Uses BFS
        Time complexity: O(MN) where M is the length of the words and N is the total
        number of words in the input list.
        Space Complexity: O(MN)
        '''
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        L = len(beginWord)
        
        #build graph (dictionary) of all words that can be formed
        graph = self.build_graph(wordList)
        
        q = deque()
        q.append((beginWord, 1))
        seen = set()
        print(graph)
        
        while len(q) > 0:
            curr_word, count = q.popleft()
            if curr_word not in seen:
                
                seen.add(curr_word)

                for i in range(L):
                    generic = curr_word[:i] + '*' + curr_word[i+1:]
                    #import pdb; pdb.set_trace()
                    for word in graph[generic]:
                        #print(word)
                        if word == endWord:
                            return count + 1
                        
                        q.append((word, count + 1))
                    
                    graph[generic] = []
        return 0
    
    def build_graph(self, wordList):
        graph = defaultdict(list)
        L = len(wordList[0])
        for word in wordList:
            for i in range(L):
                graph[word[:i] + '*' + word[i+1:]].append(word)
        return graph
    
    def ladder_length_2(self, begin_word, end_word, word_list):
        '''
        Uses a bidirectional BFS
        '''
        if end_word not in word_list or not begin_word or not end_word or not word_list:
            return 0
        
        #build graph (dictionary) of all words that can be formed
        graph = self.build_graph(word_list)
        
        q1 = deque()
        q1.append((begin_word, 1))
        q2= deque()
        q2.append((end_word, 1))
        seen1 = {}
        seen2 = {}
        while q1 and q2:
            result = self.visit_node(graph, q1, seen1, seen2)
            if result:
                return result
            result = self.visit_node(graph, q2, seen2, seen1)
            if result:
                return result
        return 0
    
    def visit_node(self, graph, queue, visited_q, other_q_visited):
        curr_word, level = queue.popleft()
        if curr_word not in visited_q:
            
            for i in range(len(curr_word)):
                generic = curr_word[:i] + '*' + curr_word[i+1:]
                for word in graph[generic]:
                    if word in other_q_visited:
                        return level + other_q_visited[word]
                    queue.append((word, level + 1))
            
            visited_q[curr_word] = level
        return None

    def ladder(self, beginWord, endWord, wordList):
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        
        L = len(beginWord)
        
        #build graph (dictionary) of all words that can be formed
        graph = self.build_graph(wordList)
        
        q = deque()
        q.append((beginWord, 1))
        seen = set()
        #print(graph)
        word_graph = defaultdict(set)
        level = {beginWord: 1}
        while len(q) > 0:
            curr_word, count = q.popleft()
            if curr_word not in seen:
                
                seen.add(curr_word)

                for i in range(L):
                    generic = curr_word[:i] + '*' + curr_word[i+1:]
                    #import pdb; pdb.set_trace()
                    for word in graph[generic]:
                        if level.get(curr_word, 0) < level.get(word, count + 1):
                            word_graph[curr_word].add(word)
                            level[word] = count + 1
                            q.append((word, count + 1))
        print(word_graph)
        res = []
        seen = set()
        self.dfs(beginWord, endWord, word_graph, seen, [], res)
        return res


    def dfs(self, node, end, graph, seen, temp, res):
        if node not in seen:
            seen.add(node)
            for nei in graph[node]:
                temp.append(nei)
                if nei == end:
                    res.append(temp + [])
                else:
                    self.dfs(nei, end, graph, seen, temp, res)
                temp.pop()

if __name__ == "__main__":
    wordlist = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    print(Solution().ladderLength('hit', 'cog', wordlist))
    print(Solution().ladderLength('a', 'c', ['a', 'b', 'c']))
    print(Solution().ladder('hit', 'cog', wordlist))
