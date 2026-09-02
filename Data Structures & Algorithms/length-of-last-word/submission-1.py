class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word = ""
        i = len(s) - 1
        while i >= 0:
            if last_word == "" and s[i] == " ":
                i -= 1
            elif s[i] == " ":
                return len(last_word)
            else:
                last_word += s[i]
                i -= 1

        return len(last_word)