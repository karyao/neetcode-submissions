class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_of_s = len(s)
        left = 0
        right = len_of_s-1

        s = s.lower()

        while left <= right:
            while not s[left].isalnum() and left < len_of_s-1:
                left += 1

            while not s[right].isalnum() and right >= 0:
                right -= 1

            if left > right:
                return True # check

            if s[left] != s[right]:
                return False 

            left += 1
            right -= 1

        return True