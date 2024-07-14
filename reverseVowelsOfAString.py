# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        stack = []
        vowels_pos = []

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                stack.append(s_list[i])
                vowels_pos.append(i)
        
        for j in vowels_pos:
            s_list[j] = stack.pop()

        return ''.join(s_list)
    

