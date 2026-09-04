class Solution {
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left: Int = 0
        var right: Int = numbers.size - 1
        var result = IntArray(2)

        while (left < right) { 
            if (numbers[right] + numbers[left] == target) { 
                result = intArrayOf(left+1, right+1)
                return result
            }
            else if (numbers[right] + numbers[left] > target) { 
                right--
            }
            else { 
                left++
            }
        }

        return result
    }
}
