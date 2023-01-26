class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licenseFreq = {}
        for char in licensePlate:
            if char.isalpha():
                licenseFreq[char.lower()] = licenseFreq.get(char.lower(), 0) + 1
                
        def isValidWord(word) -> bool:
            wordFreq = {}
            for char in word:
                wordFreq[char.lower()] = wordFreq.get(char.lower(), 0) + 1
            
            for item in licenseFreq:
                if item not in wordFreq or wordFreq[item] < licenseFreq[item]:
                    return False
            return True


        result = None

        for word in words:
            if isValidWord(word) and (result is None or len(word) < len(result)):
                result = word
        return result
