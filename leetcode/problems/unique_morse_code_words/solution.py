class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        r = set()

        for word in words:
            result = ""
            for char in word:
                result += s[ord(char) - 97]
            r.add(result)

        return len(r)
