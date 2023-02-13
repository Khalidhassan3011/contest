class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = score.copy()
        sorted_score.sort(reverse=True)
        result = []
        for num in score:
            if num == sorted_score[0]:
                result.append("Gold Medal")
            elif num == sorted_score[1]:
                result.append("Silver Medal")
            elif num == sorted_score[2]:
                result.append("Bronze Medal")
            else:
                result.append(str(sorted_score.index(num) + 1))

        return result