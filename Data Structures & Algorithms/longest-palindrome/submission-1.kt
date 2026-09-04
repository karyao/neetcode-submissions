class Solution {
    fun longestPalindrome(s: String): Int {
        // at most, there can only be one odd count of number
        var maxLength: Int = s.length
        var hashMap = HashMap<Char, Int>()
        for (c in s) { 
            hashMap[c] = (hashMap[c] ?: 0) + 1
        }
        var hasOdd: Boolean = false 
        for ((key, value) in hashMap) { 
            if ((value % 2 == 1) && !hasOdd) { 
                hasOdd = true
            } else if ((value % 2 == 1) && hasOdd) { 
                maxLength -= 1
            }
        }

        return maxLength
    }
}