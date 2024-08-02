# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/?envType=daily-question&envId=2024-08-02
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        l = 0
        current_ones, max_ones = 0, 0
        N = len(nums)
        total_ones = nums.count(1)
        for r in range(2*N):

            if nums[r%N] == 1:
                current_ones +=1
            
            if r - l + 1 > total_ones:
                current_ones -= nums[l%N]
                l+=1
            max_ones = max(max_ones, current_ones)
        
        return total_ones - max_ones
