# https://leetcode.com/problems/longest-mountain-in-array/description/
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr)<3:
            return 0
        
        res = 0
        n = len(arr)
        for i in range(1, n-1):
        
            if arr[i-1] < arr[i] > arr[i+1]:
                left, right = i-1, i+1

                while left-1>0 and arr[left-1]<arr[left]:
                    left-=1
                
                while right+1<n and arr[right+1] < arr[right]:
                    right+=1
                
                res = max(res, right-left +1)
        

        return res 
