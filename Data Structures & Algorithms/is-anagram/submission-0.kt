class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        // If length is not same, cannot be anagram
        if (s.length != t.length) { 
            return false
        }

        var s_sorted = s.toCharArray().sorted().joinToString("")
        var t_sorted = t.toCharArray().sorted().joinToString("")

        return s_sorted == t_sorted
    }
}
