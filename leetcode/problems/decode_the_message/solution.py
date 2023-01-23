from collections import OrderedDict

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        combine = {}
        letter = 97
        for char in key:
            if len(combine) == 26:
                break
            if char == " ":
                continue

            if char not in combine:
                combine[char] = chr(letter)
                letter += 1
            

        result = ""
        for char in message:
            result += combine.get(char,  " ")
        
        return result



        

