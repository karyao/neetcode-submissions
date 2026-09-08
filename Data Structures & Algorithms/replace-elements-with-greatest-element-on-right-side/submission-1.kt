class Solution {
    fun replaceElements(arr: IntArray): IntArray {
        // for every value, get the max value on it's left and replace.
        for ((i, a) in arr.withIndex()) { 
            var maxValue: Int = Int.MIN_VALUE
            for (j in i+1 until arr.size) { 
                maxValue = max(maxValue, arr[j])
            }
            arr[i] = maxValue
        }

        // replace last value with -1 
        arr[arr.size-1] = -1
        return arr
    }
}
