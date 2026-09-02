class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        i = 0
        for n in nums:
            sub = target - n
            if sub in hashmap:
                return [hashmap[sub], i]

            hashmap[n] = i
            i += 1

        return []
            