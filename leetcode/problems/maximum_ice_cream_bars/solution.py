class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        r = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                break
            r += 1
        return r
