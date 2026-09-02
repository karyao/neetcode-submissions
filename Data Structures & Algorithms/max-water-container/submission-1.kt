class Solution {
    fun maxArea(height: IntArray): Int {
        var maxWidth: Int = 0
        var left: Int = 0
        var right: Int = height.size - 1
        while (left < right) { 
            var lowerLine: Int = 0
            if (height[left] < height[right]) { 
                lowerLine = height[left]
            } else { 
                lowerLine = height[right]
            }
            var tempWidth: Int = lowerLine * (right - left)
            maxWidth = max(maxWidth, tempWidth)

            if (height[left] < height[right]) { 
                left++
            } else {
                right--
            }
        }

        return maxWidth
    }
}
