class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq = {}
        for i, v in enumerate(list1):
            if v in list2:
                freq[v] = i + list2.index(v)

        result = []
        low = 0
        for item in freq:
            if freq[item] < low:
                result.clear()

            if not result or low == freq[item]:
                result.append(item)
                low = freq[item]
        
        return result



