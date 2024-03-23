# https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        if s == t:
            return s

        map_t = {}

        for c in t:
            map_t[c] = 1 + map_t.get(c, 0)

        have, need = 0, len(map_t)

        res, res_l = (-1, 1), float("inf")

        map_s = {}
        l = 0
        for r in range(len(s)):
            char = s[r]
            map_s[char] = 1 + map_s.get(char, 0)

            if char in map_t and map_s[char] == map_t[char]:
                have += 1
            
            while have == need:
                if r - l + 1 < res_l:
                    res = (l, r)
                    res_l = r - l + 1

                if s[l] in map_t:
                    map_s[s[l]] -= 1
                    if map_s[s[l]] < map_t[s[l]]:
                        have -= 1
                
                l += 1

        l, r = res

        return s[l:r + 1] if res_l != float("inf") else ""
