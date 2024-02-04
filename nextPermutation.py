# https://leetcode.com/problems/next-permutation/
# a = [2, 1, 5, 4, 3, 0, 0]

# dip = None
# for i in range(len(a) - 2, -1, -1):
#     print(i)
#     if a[i] < a[i + 1]:
#         dip = i
#         break

# if dip is not None:
#     for i in range(len(a) - 1, dip, -1):
#         if a[i] > a[dip]:
#             a[i], a[dip] = a[dip], a[i]
#             break

# a = a[:dip + 1] + a[dip + 1:][::-1]
# print(a)



        


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        dip = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                dip = i
                break

        if dip ==-1:
            return nums.sort()
    
        for i in range(n-1, dip, -1):
            if nums[i] > nums[dip]:
                nums[i], nums[dip] = nums[dip], nums[i]
                break
            # Reverse the suffix
        nums[dip+1:] = reversed(nums[dip+1:])

        return nums
        