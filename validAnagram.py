# https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_mpp = Counter(s)
        # t_mpp = Counter(t)

        # return s_mpp == t_mpp

        ###############
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(t[i])- ord('a')] -=1
            count[ord(s[i])- ord('a')] +=1

        for i in range(len(count)):

            if count[i] !=0:
                return False
        
        return True
