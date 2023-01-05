class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)
        ans = 1
        nextEnd = points[0][0]
        for item in points:
            if item[1] < nextEnd:
                ans += 1
                nextEnd = item[0]

        return ans