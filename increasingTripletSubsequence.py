# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # update first if num is smaller than first
            elif num <= second:
                second = num  # update second if num is between first and second
            else:
                return True  # return true if num is greater than both first and second
        
        return False  # no such triplet found
