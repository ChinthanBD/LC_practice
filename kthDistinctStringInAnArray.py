# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/?envType=daily-question&envId=2024-08-05
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mpp = {}

        for s in arr:
            mpp[s] = mpp.get(s, 0) + 1

        ans = []
        for s, freq in mpp.items():
            if freq==1:
                ans.append(s)
        

        return ans[k-1] if k <= len(ans) else ""
                 
        
