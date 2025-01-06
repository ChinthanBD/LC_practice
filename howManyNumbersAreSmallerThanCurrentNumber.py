# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)

        count_dict = {}
        for i, val in enumerate(temp):
            if val not in count_dict:
                count_dict[val] = i
        res=[]
        for n in nums:
            res.append(count_dict[n])
        
        return res
                
