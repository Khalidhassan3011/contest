from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key: List[str] = ["type", "color", "name"]

        result: int = 0

        for item in items:
            if item[key.index(ruleKey)] == ruleValue:
                result += 1

        return result


s = Solution()
a = s.countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                   ruleKey="color", ruleValue="silver")
print(a)
print(a == 1)

a = s.countMatches(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                   ruleKey="type", ruleValue="phone")
print(a)
print(a == 2)
