class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 1
        score = 0
        while i < len(s):
            score += abs(ord(s[i]) - ord(s[i-1]))
            i += 1

        return score