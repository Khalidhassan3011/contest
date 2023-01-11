class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            targetRow = rows[0]
            if word[0].lower() in rows[1]: targetRow = rows[1]
            if word[0].lower() in rows[2]: targetRow = rows[2]

            valid = True
            for char in word.lower():
                if char not in targetRow:
                    valid = False
            
            if valid: result.append(word)

        return result
