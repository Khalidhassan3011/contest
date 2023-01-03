class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        countRemoveColumn = 0
        for indexOfStr in range(len(strs[0])):
            for indexOfAra in range(len(strs) - 1):
                if strs[indexOfAra][indexOfStr] > strs[indexOfAra + 1][indexOfStr]:
                    countRemoveColumn += 1
                    break

        return countRemoveColumn

