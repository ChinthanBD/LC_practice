# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # res = len(s.split()[-1])
        # return res

    ########################
        last_word_length = 0
        
        for char in reversed(s):
            # If we encounter a space and we have already counted the last word
            # then break the loop
            if char == ' ' and last_word_length > 0:
                break
            # If the current character is not a space, increment the length of the last word
            elif char != ' ':
                last_word_length += 1
            # If we encounter a space and we haven't counted any characters yet, continue
            elif last_word_length == 0:
                continue
                

        
        return last_word_length