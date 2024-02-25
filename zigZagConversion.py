# https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        res = [[] for _ in range(numRows)]
        i = 0
        flag = 1
        for char in s:
            res[i].append(char)
            if i ==0:
                flag = 1
            elif i == numRows -1:
                flag = -1
            
            i += flag
    
        output = []
        for row in res:
            output += row
        
        output = ''.join(output)

        return output
            