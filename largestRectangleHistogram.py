# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        prev_smallest = [-1] * n
        next_smallest = [n] * n

        # Find previous smallest element for each element
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                prev_smallest[i] = stack[-1]
            stack.append(i)
        
        # Find next smallest element for each element
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                next_smallest[i] = stack[-1]
            stack.append(i)


        # below piece of code can be written in the above 2nd for loop itself to reduce the number of pass
        # Calculate max area
        max_area = 0
        for i in range(n):
            width = next_smallest[i] - prev_smallest[i] - 1
            max_area = max(max_area, width * heights[i])
        
        return max_area
