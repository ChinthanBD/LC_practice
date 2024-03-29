# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_mpp = Counter(s)
        t_mpp = Counter(t)

        if s_mpp == t_mpp:
            return True
        return False