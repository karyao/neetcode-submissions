class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consecutive_len = 1
        temp_consecutive_len = 1
        unique_nums = sorted(list(set(nums)))

        for i in range(1, len(unique_nums)):
            if (unique_nums[i]) == (unique_nums[i-1] + 1):
                temp_consecutive_len += 1
            else:
                consecutive_len = max(consecutive_len, temp_consecutive_len)
                temp_consecutive_len = 1

        consecutive_len = max(consecutive_len, temp_consecutive_len)
        return consecutive_len if len(nums) != 0 else 0