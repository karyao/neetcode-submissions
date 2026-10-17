class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones.sort(reverse=True)
        while stones[1] != 0:
            if stones[0] == stones[1]:
                stones[0] = 0
            else:
                stones[0] = stones[0] - stones[1]
            stones[1] = 0
            stones.sort(reverse=True) 

        return stones[0]