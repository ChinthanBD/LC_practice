# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        while l<len(s) and r<len(t):
            if s[l] == t[r]:
                l +=1
            r+=1

        if l<len(s):
            return False
        return True