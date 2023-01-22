# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, hi = 1, n
        while low < hi:
            mid = low + (hi - low) // 2
            if isBadVersion(mid): hi = mid
            else : low = mid + 1
        return low
            