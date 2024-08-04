# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/?envType=daily-question&envId=2024-08-04
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        arr = []
        n = len(nums)
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                arr.append(curr_sum)
        
        arr.sort()
        ans = 0
        for i in range(left-1, right):
            ans = (ans + arr[i]) % MOD
        
        return ans
