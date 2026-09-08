class Solution {
    fun maxProductDifference(nums: IntArray): Int {
        // two biggest numbers * two smallest numbers = maximum product
        nums.sort() 

        val firstProduct = nums[0] * nums[1]
        val secondProduct = nums[nums.size-1] * nums[nums.size-2]

        return secondProduct - firstProduct
    }
}