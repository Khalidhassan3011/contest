from collections import OrderedDict

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:


        # METHOD 1

        # letters = {}

        # # ascii value of a
        # lastLetterInsert = 97 

        # for keyCharecter in key:
        #     if keyCharecter == " ":
        #         continue

        #     if keyCharecter not in letters:
        #         letters[keyCharecter] = chr(lastLetterInsert)
        #         lastLetterInsert += 1
            
        #     if len(letters) == 26 or lastLetterInsert == 123:
        #         break;

        # result = ""
        # for charecter in message:
        #     if charecter == " ":
        #         result += charecter
        #     else:
        #         result += letters[charecter]
        
        # return result



        # METHOD 2

        decode = dict(zip("".join(OrderedDict.fromkeys(key.replace(" ",""))), "abcdefghijklmnopqrstuvwxyz"))

        return "".join(decode.get(c, " ") for c in message)

        

