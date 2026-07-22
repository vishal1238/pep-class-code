# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.Example:Input: nums = [1,1,1,2,2,3], k = 2Output: [1, 2]


from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]


# Example
nums = [1, 1, 1, 2, 2, 3]
k = 2

obj = Solution()
print(obj.topKFrequent(nums, k))