# https://leetcode.com/problems/neighboring-bitwise-xor/?envType=daily-question&envId=2025-01-17
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        helper = [0]
        n=len(derived)
        for i in range(1, n):                
            if derived[i-1] == 1:
                helper.append(not helper[i-1])
            else:
                helper.append(helper[i-1])

        if derived[n-1] == 1 and helper[0] == helper[n-1]:
            return False
        
        if derived[n-1] == 0 and helper[0] != helper[n-1]:
            return False
        
        return True


##################################
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        last = 0
        for n in derived:
            if n:
                last = ~last
        
        return first == last
