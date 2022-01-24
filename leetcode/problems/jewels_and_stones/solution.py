class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count: int = 0
        for letter in jewels:
            count += stones.count(letter)

        return count
