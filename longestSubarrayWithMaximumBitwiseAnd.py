# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/?envType=daily-question&envId=2024-09-14

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_max = float("-inf")
        res = 0
        count = 0  # to count the length of the subarray of max elements
        
        for n in nums:
            if n > curr_max:
                curr_max = n  # update the maximum value
                count = 1  # reset the count since we found a new max
            elif n == curr_max:
                count += 1  # extend the subarray
            else:
                count = 0  # reset the count if n is less than curr_max
                
            res = max(res, count)  
        return res



    # def longestSubarray(self, nums: List[int]) -> int:
    #     return max((v,len([*p])) for v,p in groupby(nums))[1]

    # def longestSubarray(self, a):
    #     return max(accumulate([0]+a,lambda l,v,M=max(a):(l+1)*(v==M)))
