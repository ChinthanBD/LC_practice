# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        sum_val = (n * (n+1)) //2    # be careful about the brackets and BODMAS
        print(sum_val)
        return sum_val - sum(nums)
