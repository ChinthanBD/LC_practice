# https://leetcode.com/problems/minimum-absolute-difference/description/
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        ans = []
        min_val = float("inf")
        for i in range(n-1):
            j = i+1
            if arr[j]-arr[i]< min_val:
                ans=[[arr[i], arr[j]]]
                min_val = arr[j]-arr[i]
            
            elif arr[j]-arr[i] == min_val:
                ans.append([arr[i],arr[j]])
        
        return ans

