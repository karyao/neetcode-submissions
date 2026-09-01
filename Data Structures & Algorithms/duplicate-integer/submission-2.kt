class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        val numsSet = nums.toSet()
        return nums.size != numsSet.size
    }
}
