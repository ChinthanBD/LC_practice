# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        mpp = {'a': -1, 'b': -1, 'c': -1}
        for i in range(len(s)):
            mpp[s[i]] = i  # Update the last position of the character
            
            # Once we have seen all three characters, we can count the number of substrings
            if all(mpp[char] != -1 for char in 'abc'):
                ans += min(mpp.values()) + 1  # +1 because we want the count of valid substrings
        
        return ans


