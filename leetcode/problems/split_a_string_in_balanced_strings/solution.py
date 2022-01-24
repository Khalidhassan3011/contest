class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, ans = 0, 0, 0

        for v in s:
            if v == "L":
                l += 1
            else:
                r += 1

            if l == r:
                ans += 1

        return ans