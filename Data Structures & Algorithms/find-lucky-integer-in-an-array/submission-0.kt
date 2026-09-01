class Solution {
    fun findLucky(arr: IntArray): Int {
        var freq = hashMapOf<Int, Int>() 
        for (num in arr) { 
            freq[num] = freq.getOrDefault(num, 0) + 1  
        }
        var maxKey = -1
        for ((key, value) in freq) { 
            if (key == value){ 
                if (maxKey == -1 || maxKey < value) { 
                    maxKey = value 
                }
            }
        }
        return maxKey
    }
}
