# You are given an array of integers nums, and there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position, return the max value present inside that sliding window.Constraint: You must solve it in O(n) time complexity.Example:Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3Output: [3, 3, 5, 5, 6, 7]


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # Store the maximum for the current window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Example
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

obj = Solution()
print(obj.maxSlidingWindow(nums, k))