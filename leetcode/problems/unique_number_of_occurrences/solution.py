class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}

        result = {}

        for item in arr:
            count[item] = count.get(item, 0) + 1

        for key, value in count.items():
            if count[key] in result.keys():
                return False
            else:
                result[count[key]] = count[key]

        return True

