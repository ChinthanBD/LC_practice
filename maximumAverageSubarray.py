# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_sum = sum(nums[:k])
        ans = curr_sum


        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            ans = max(ans, curr_sum)
        return ans /float(k)


