class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        key: List[str] = ["type", "color", "name"]

        result: int = 0

        for item in items:
            if item[key.index(ruleKey)] == ruleValue:
                result += 1

        return result