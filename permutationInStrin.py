# https://leetcode.com/problems/permutation-in-string/description/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mpp1 = {}
        mpp2 = {}
        
        # Initialize frequency dictionaries
        for i in range(len(s1)):
            mpp1[s1[i]] = 1 + mpp1.get(s1[i], 0)
            mpp2[s2[i]] = 1 + mpp2.get(s2[i], 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if mpp1 == mpp2:
                return True
            # Slide the window
            mpp2[s2[r]] = 1 + mpp2.get(s2[r], 0)
            mpp2[s2[l]] -= 1
            if mpp2[s2[l]] == 0:
                del mpp2[s2[l]]
            l += 1
        
        # Check the last window
        return mpp1 == mpp2
