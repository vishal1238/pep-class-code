# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, find the area of the largest rectangle in the histogram.Example:Input: heights = [2, 1, 5, 6, 2, 3]Output: 10 (The largest rectangle is formed by bars 5 and 6 with a shared height of 5 and width of 2).


class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # Stores (start_index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
x
            stack.append((start, h))

        n = len(heights)

        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (n - index))

        return max_area


# Example
heights = [2, 1, 5, 6, 2, 3]

obj = Solution()
print(obj.largestRectangleArea(heights))