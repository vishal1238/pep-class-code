# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the i-th line are (i, 0) and \((i, \text{height}[i])\).Find two lines that together with the x-axis form a container, such that the container contains the most water. Return the maximum amount of water a container can store.Example:Input: height = [1,8,6,2,5,4,8,3,7]Output: 49 (Width between first 8 and 7 is 7, height is bounded by 7 → 7 × 7 = 49)


class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

obj = Solution()
print(obj.maxArea(height))