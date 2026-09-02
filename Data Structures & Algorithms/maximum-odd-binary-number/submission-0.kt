class Solution {
    fun maximumOddBinaryNumber(s: String): String {
        var numOfSetBits: Int = 0
        for (c in s) { 
            if (c == '1') {
                numOfSetBits += 1
            }
        }
        var lenOfs: Int = s.length
        var newS: String = ""
        while (numOfSetBits > 1) { 
            newS += '1'
            numOfSetBits--
        }
        var remainingZeros: Int = lenOfs - newS.length
        while (remainingZeros > 1) { 
            newS += '0'
            remainingZeros--
        }
        if (numOfSetBits == 0) { 
            newS += '0'
        } else { 
            newS += '1'
        }
        return newS
    }
}
