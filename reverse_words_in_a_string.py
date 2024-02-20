# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        l = 0
        r = len(lst) -1
        while l<r:
            lst[l], lst[r] = lst[r],lst[l]
            l +=1
            r-=1
	 	
        res = ' '.join(lst)
        return res