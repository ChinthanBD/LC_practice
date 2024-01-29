# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        right = 0
        left = 0
        mpp = {}

        while right< len(s):
            if s[right] in mpp:
                left = max(left, mpp[s[right]] + 1)
            mpp[s[right]] = right
            right +=1
            res = max(res, right -left)
        return res
