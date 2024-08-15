# https://leetcode.com/problems/lemonade-change/?envType=daily-question&envId=2024-08-15
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bills, ten_bills = 0, 0

        for bill in bills:
            if bill == 5:
                five_bills+=1
                
            elif bill == 10:
                if five_bills > 0:
                    five_bills -=1
                    ten_bills +=1
                else:
                     return False
            else:              
                if five_bills > 0 and ten_bills>0:
                    five_bills -=1
                    ten_bills -=1
                elif five_bills >=3:
                    five_bills -=3            
                else:
                    return False
        
        return True




