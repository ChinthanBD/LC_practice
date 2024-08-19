# https://leetcode.com/problems/2-keys-keyboard/submissions/1361436573/?envType=daily-question&envId=2024-08-19
class Solution:
    def minSteps(self, n: int) -> int:
        cache = {}
        def helper(count, paste):

            if (count, paste) in cache:
                return cache[(count, paste)]
            if count == n:
                return 0
            
            elif count>n:
                return 1000 # ideally float("inf") but using 1000 since the constraints specify 1000

            # just paste
            res1 = 1 + helper(count+paste, paste)

            # copy + paste

            res2 = 2 + helper(count + count, count)
            cache[(count, paste)] = min(res1, res2)
            return cache[(count, paste)]
        if n == 1:
            return 0
        
        return 1 + helper(1, 1)
