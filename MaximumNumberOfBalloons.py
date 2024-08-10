class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mpp = Counter(text)

        # Initialize ans with a large value
        ans = float("inf")

        # For each character in "balloon", calculate the possible number of balloons
        for ch in "balon":
            if ch == 'l' or ch == 'o':
                ans = min(ans, mpp[ch] // 2)
            else:
                ans = min(ans, mpp[ch])

        return ans
