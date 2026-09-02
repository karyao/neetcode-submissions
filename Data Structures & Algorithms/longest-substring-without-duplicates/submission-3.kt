class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
        var tempSeq: String = ""
        var maxLength: Int = 0
        var tempLength: Int = 0
        for (c in s) { 
            if (c !in tempSeq) {
                tempLength++
            } else { 
                while (!tempSeq.isEmpty() && (c in tempSeq)) { 
                    tempSeq = tempSeq.drop(1)
                }
                maxLength = max(maxLength, tempLength)
                tempLength = tempSeq.length + 1
            }
            tempSeq += c
        }
        maxLength = max(maxLength, tempLength)
        return maxLength
    }
}
