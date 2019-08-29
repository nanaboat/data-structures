'''
Find Median from Data Stream
Hard

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

    void addNum(int num) - Add a integer number from the data stream to the data structure.
    double findMedian() - Return the median of all elements so far.

 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2

 

Follow up:

    If all integer numbers from the stream are between 0 and 100, how would you optimize it?
    If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?


'''
'''
Approach 3: Two Heaps

Intuition

The above two approaches gave us some valuable insights on how to tackle this problem. Concretely, one can infer two things:

    If we could maintain direct access to median elements at all times, then finding the median would take a constant amount of time.
    If we could find a reasonably fast way of adding numbers to our containers, additional penalties incurred could be lessened.

But perhaps the most important insight, which is not readily observable, is the fact that we only need a consistent way to access the median elements. Keeping the entire input sorted is not a requirement.

    Well, if only there were a data structure which could handle our needs.

As it turns out there are two data structures for the job:

    Heaps (or Priority Queues [1])
    Self-balancing Binary Search Trees (we'll talk more about them in Approach 4)

Heaps are a natural ingredient for this dish! Adding elements to them take logarithmic order of time. They also give direct access to the maximal/minimal elements in a group.

If we could maintain two heaps in the following way:

    A max-heap to store the smaller half of the input numbers
    A min-heap to store the larger half of the input numbers

This gives access to median values in the input: they comprise the top of the heaps!

Wait, what? How?

If the following conditions are met:

    Both the heaps are balanced (or nearly balanced)
    The max-heap contains all the smaller numbers while the min-heap contains all the larger numbers

then we can say that:

    All the numbers in the max-heap are smaller or equal to the top element of the max-heap (let's call it xxx)
    All the numbers in the min-heap are larger or equal to the top element of the min-heap (let's call it yyy)

Then xxx and/or yyy are smaller than (or equal to) almost half of the elements and larger than (or equal to) the other half. That is the definition of median elements.

This leads us to a huge point of pain in this approach: balancing the two heaps!

Algorithm

    Two priority queues:
        A max-heap lo to store the smaller half of the numbers
        A min-heap hi to store the larger half of the numbers

    The max-heap lo is allowed to store, at worst, one more element more than the min-heap hi. Hence if we have processed kkk elements:
        If k=2∗n+1(∀ n∈Z)k = 2*n + 1 \quad (\forall \, n \in \mathbb{Z})k=2∗n+1(∀n∈Z), then lo is allowed to hold n+1n+1n+1 elements, while hi can hold nnn elements.
        If k=2∗n(∀ n∈Z)k = 2*n \quad (\forall \, n \in \mathbb{Z})k=2∗n(∀n∈Z), then both heaps are balanced and hold nnn elements each.

    This gives us the nice property that when the heaps are perfectly balanced, the median can be derived from the tops of both heaps. Otherwise, the top of the max-heap lo holds the legitimate median.

    Adding a number num:
        Add num to max-heap lo. Since lo received a new element, we must do a balancing step for hi. So remove the largest element from lo and offer it to hi.
        The min-heap hi might end holding more elements than the max-heap lo, after the previous operation. We fix that by removing the smallest element from hi and offering it to lo.

    The above step ensures that we do not disturb the nice little size property we just mentioned.

A little example will clear this up! Say we take input from the stream [41, 35, 62, 5, 97, 108]. The run-though of the algorithm looks like this:

Adding number 41
MaxHeap lo: [41]           // MaxHeap stores the largest value at the top (index 0)
MinHeap hi: []             // MinHeap stores the smallest value at the top (index 0)
Median is 41
=======================
Adding number 35
MaxHeap lo: [35]
MinHeap hi: [41]
Median is 38
=======================
Adding number 62
MaxHeap lo: [41, 35]
MinHeap hi: [62]
Median is 41
=======================
Adding number 4
MaxHeap lo: [35, 4]
MinHeap hi: [41, 62]
Median is 38
=======================
Adding number 97
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97]
Median is 41
=======================
Adding number 108
MaxHeap lo: [41, 35, 4]
MinHeap hi: [62, 97, 108]
Median is 51.5

Complexity Analysis

    Time complexity: O(5⋅log⁡n)+O(1)≈O(log⁡n)O(5 \cdot \log n) + O(1) \approx O(\log n)O(5⋅logn)+O(1)≈O(logn).
        At worst, there are three heap insertions and two heap deletions from the top. Each of these takes about O(log⁡n)O(\log n)O(logn) time.
        Finding the mean takes constant O(1)O(1)O(1) time since the tops of heaps are directly accessible.

    Space complexity: O(n)O(n)O(n) linear space to hold input in containers.
https://leetcode.com/problems/find-median-from-data-stream/solution/

'''

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num: int) -> None:
        val = heapq.heappushpop(self.maxheap, -1 * num)
        heapq.heappush(self.minheap, (val * -1))
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0] * - 1.0
        
        return ((self.maxheap[0] * - 1) + self.minheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''
Approach 4: Multiset and Two Pointers

Intuition

Self-balancing Binary Search Trees (like an AVL Tree) have some very interesting properties. They maintain the tree's height to a logarithmic bound. Thus inserting a new element has reasonably good time performance. The median always winds up in the root of the tree and/or one of its children. Solving this problem using the same approach as Approach 3 but using a Self-balancing BST seems like a good choice. Except the fact that implementing such a tree is not trivial and prone to errors.

Why reinvent the wheel? Most languages implement a multiset class which emulates such behavior. The only problem remains keeping track of the median elements. That is easily solved with pointers! [2]

We maintain two pointers: one for the lower median element and the other for the higher median element. When the total number of elements is odd, both the pointers point to the same median element (since there is only one median in this case). When the number of elements is even, the pointers point to two consecutive elements, whose mean is the representative median of the input.

Algorithm

    Two iterators/pointers lo_median and hi_median, which iterate over the data multiset.

    While adding a number num, three cases arise:

        The container is currently empty. Hence we simply insert num and set both pointers to point to this element.

        The container currently holds an odd number of elements. This means that both the pointers currently point to the same element.
            If num is not equal to the current median element, then num goes on either side of it. Whichever side it goes, the size of that part increases and hence the corresponding pointer is updated. For example, if num is less than the median element, the size of the lesser half of input increases by 111 on inserting num. Thus it makes sense to decrement lo_median.
            If num is equal to the current median element, then the action taken is dependent on how num is inserted into data. NOTE: In our given C++ code example, std::multiset::insert inserts an element after all elements of equal value. Hence we increment hi_median.

        The container currently holds an even number of elements. This means that the pointers currently point to consecutive elements.
            If num is a number between both median elements, then num becomes the new median. Both pointers must point to it.
            Otherwise, num increases the size of either the lesser or higher half of the input. We update the pointers accordingly. It is important to remember that both the pointers must point to the same element now.

    Finding the median is easy! It is simply the mean of the elements pointed to by the two pointers lo_median and hi_median.

'''