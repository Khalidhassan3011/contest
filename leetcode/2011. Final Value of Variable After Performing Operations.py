from typing import List


class Solution:
    def method2(self, operations: List[str]) -> int:
        count: int = 0

        for v in operations:
            if v == "X++" or v == "++X":
                count += 1
            else:
                count -= 1

        return count

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # return self.method1(operations)
        return self.method2(operations)


s = Solution()
print(s.finalValueAfterOperations(["--X", "X++", "X++"]))
