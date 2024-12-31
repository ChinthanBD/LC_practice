#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #approach
        #-> find length of array and create dict/set of input
        #-> iterate over the range and create a res of missing numbers

        res = []
        nums_set = set(nums)

        for i in range(1, len(nums)+1):
            if i not in nums_set:
                res.append(i)
        
        return res
