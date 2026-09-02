class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        min_word_count = len(strs[0])
        for w in strs:
            if min_word_count > len(w):
                min_word_count = len(w)
        
        for i in range(min_word_count):
            c = strs[0][i]
            for w in strs:
                if w[i] != c:
                    return prefix
            prefix += c

        return prefix 