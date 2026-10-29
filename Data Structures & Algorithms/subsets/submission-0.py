class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []

        def explore(i):
            if i == len(nums):
                results.append(path.copy())
                return 

            path.append(nums[i])
            explore(i+1)
            path.pop()

            explore(i+1)

        explore(0)
        return results 