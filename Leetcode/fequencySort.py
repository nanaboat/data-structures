'''
Given an array return a custom sort based on the frequency
'''
from collections import Counter, OrderedDict
import heapq

def customSort(arr):
    h_map = Counter(arr)
    heap = [(-f, v) for v, f in h_map.items()]
    heapq.heapify(heap)
    result = []
    for i in range(len(heap)):
        f, v = heapq.heappop(heap)
        result += ([v] * (-1 * f))

    return result


class Solution:
    '''
    692. Top K Frequent Words
Medium

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Input words contain only lowercase letters.

Follow up:

    Try to solve it in O(n log k) time and O(n) extra space.
https://leetcode.com/problems/top-k-frequent-words/

    '''
    def topKFrequent(self, word, k):
        h_map = Counter(word)
        #r = heapq.nlargest(k, h_map.keys(), key=h_map.get)
        heap = [(-freq, word) for word, freq in h_map.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for w in range(k)]

if __name__ == "__main__":
    nums = [8, 5, 5, 5, 5, 1, 1, 1, 4, 4, 6]
    print(customSort(nums))
