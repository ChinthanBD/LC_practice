# https://leetcode.com/problems/isomorphic-strings/submissions/1190801010/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_mpp = {}
        t_mpp = {}

        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

            if (c1 in s_mpp and s_mpp[c1] != c2) or (c2 in t_mpp and t_mpp[c2] !=c1):
                return False
            s_mpp[c1] = c2
            t_mpp[c2] = c1 

        return True       