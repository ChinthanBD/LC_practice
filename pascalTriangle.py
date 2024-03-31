# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        # Initialize the result with the first row
        result = [[1]]
        
        for i in range(1, numRows):
            row = [1]  # First element of each row is always 1
            for j in range(1, i):  # Calculate the elements in between
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)  # Last element of each row is always 1
            result.append(row)
        
        return result


##########################
    #def generate(self, numRows: int) -> List[List[int]]:
    #    result = []
    #    for row in range(1, numRows + 1):
    #        current_row = []
    #        for column in range(1, row + 1):
    #            # Calculate the element using the combination formula
    #            element = self.combination(row - 1, column - 1)
    #            current_row.append(element)
    #        result.append(current_row)
    #    return result
    #
    #def combination(self, n: int, k: int) -> int:
    #    # Calculate n choose k
    #    numerator = 1
    #    denominator = 1
    #    for i in range(k):
    #        numerator *= n - i
    #        denominator *= i + 1
    #    return numerator // denominator


#############################
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        
        for i in range(1, numRows):
            row = []
            for j in range(i+1):
                left = 0 
                right = 0
                if j-1>=0:
                    left = res[i-1][j-1]
                if j < len(res[i - 1]):
                    right = res[i-1][j]
                val = left + right
                row.append(val)
            res.append(row)
        
        return res

