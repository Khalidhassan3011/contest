class Solution:
    def firstUniqChar(self, s: str) -> int:
        letterCountAndPosition = {}

        for index, charecter in enumerate(s):
            letterCountAndPosition[charecter] = {
                "count": letterCountAndPosition[charecter]["count"] + 1 if charecter in letterCountAndPosition else 1,
                "lastIndex": index
            }

        for charecter, value in letterCountAndPosition.items():
            if value["count"] == 1 :
                return value["lastIndex"]

        return -1
            