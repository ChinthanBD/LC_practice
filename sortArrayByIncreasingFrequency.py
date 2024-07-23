# https://leetcode.com/problems/sort-array-by-increasing-frequency/?envType=daily-question&envId=2024-07-23
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return sorted(nums, key=lambda x: (count[x], -x))
