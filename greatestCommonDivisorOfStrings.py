# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Compute the gcd of the lengths of str1 and str2
        len1, len2 = len(str1), len(str2)
        gcd_len = gcd(len1, len2)
        
        # Candidate substring that might be the gcd string
        candidate = str1[:gcd_len]
        
        # Check if the candidate divides both strings
        if str1 == candidate * (len1 // gcd_len) and str2 == candidate * (len2 // gcd_len):
            return candidate
        return ""