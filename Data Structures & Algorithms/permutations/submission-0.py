class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []

        def explore():
            if len(path) == len(nums):
                results.append(path.copy())
                return 

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                explore()
                path.pop()

        explore()

        return results 