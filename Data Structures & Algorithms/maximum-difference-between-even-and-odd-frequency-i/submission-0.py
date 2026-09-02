from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()

        odds = []
        evens = []

        for c in counts:
            if c % 2 !=0 :
                odds.append(c)
            else:
                evens.append(c)

        return max(odds) - min(evens)