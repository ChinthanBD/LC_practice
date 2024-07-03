# https://leetcode.com/problems/intersection-of-two-arrays-ii/?envType=daily-question&envId=2024-07-02
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Count the occurrences of each element in nums1
        counts = Counter(nums1)
        
        # Result list to store the intersection
        ans = []
        
        # Iterate over nums2 and find common elements
        for num in nums2:
            if counts[num] > 0:
                ans.append(num)
                counts[num] -= 1
        
        return ans
