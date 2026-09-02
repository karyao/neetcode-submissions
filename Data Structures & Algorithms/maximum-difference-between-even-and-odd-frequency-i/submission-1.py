class Solution:
    def maxDifference(self, s: str) -> int:
        frequency = {}

        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        
        max_odd = 0
        min_even = float("inf")

        for count in frequency.values():
            if count % 2 == 1:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)

        return max_odd - min_even