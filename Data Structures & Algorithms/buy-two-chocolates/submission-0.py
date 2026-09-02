class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()

        chocolate_price = prices[1] + prices[0]
        if chocolate_price > money:
            return money

        return money - chocolate_price
        