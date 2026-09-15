class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(0, k):
            gifts.sort()
            gifts[-1] = int(sqrt(gifts[-1]))

        num_of_gifts = sum(gifts)
        return num_of_gifts 
