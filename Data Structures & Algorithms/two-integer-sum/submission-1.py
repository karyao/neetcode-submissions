class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # value -> index
        sol = []
        i = 0
        for n in nums: 
            complement = target - n
            # check if exist in existing subtraction
            if complement in hashmap:
                return [hashmap[complement], i]

            # if not add to dict with index
            hashmap[n] = i
            i += 1

        return sol

