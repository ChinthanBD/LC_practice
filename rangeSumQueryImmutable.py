# https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = [0] * (len(nums) +1)
        for i in range(1, len(nums)+1):
            self.prefixsum[i] = self.prefixsum[i-1] + nums[i-1]


    def sumRange(self, left: int, right: int) -> int:
        return self.prefixsum[right+1] - self.prefixsum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
