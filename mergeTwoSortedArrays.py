# https://leetcode.com/problems/merge-sorted-array/description/
class Solution:

    def swapIfGreater(self, nums1, nums2, left,right):
        if nums1[left]>nums2[right]:
            nums1[left],nums2[right] = nums2[right], nums1[left]


    def merge(self, nums1: List[int], n: int, nums2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ## Sol 1
        # nums1[m:] = nums2
        # nums1.sort()

        ## Sol 2
        length = m + n
        gap = (length)//2 + (length) %2

        while gap>0:
            left = 0
            right = left + gap

            while right < length:
                if left<n and right>=n:
                    self.swapIfGreater(nums1, nums2, left,right-n)
                elif left >n:
                    self.swapIfGreater(nums2, nums2, left-n,right-n)
                else:
                    self.swapIfGreater(nums1, nums1, left,right)
                right +=1
                left +=1
            
            if gap == 1:
                break
            gap = gap //2 + gap %2
        
        for i in range(m):
            nums1[n+i] = nums2[i]
        