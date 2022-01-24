class Solution:
    def method1(self, operations: List[str]) -> int:
        count_pos_b = operations.count("++X")
        count_pos_a = operations.count("X++")
        count_neg_b = operations.count("--X")
        count_neg_a = operations.count("X--")

        return count_pos_a + count_pos_b - count_neg_b - count_neg_a

    def method2(self, operations: List[str]) -> int:
        count: int = 0

        for v in operations:
            if v == "X++" or v == "++X":
                count += 1
            else:
                count -= 1

        return count

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        return self.method1(operations)
        # return self.method2(operations)
