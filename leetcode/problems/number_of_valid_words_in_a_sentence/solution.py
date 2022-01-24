class Solution:
    def countValidWords(self, sentence: str) -> int:
        punctuation = ['!', '.', ',']
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        hyphen = "-"

        valid: int = 0

        words = sentence.split(" ")
        for temp in words:

            if len(temp) == 0:
                continue

            if len(temp) == 1 and temp in punctuation:
                valid += 1
            elif temp[0] in punctuation or any(ele in numbers for ele in temp):
                continue
            elif temp.count(hyphen) > 1:
                continue
            elif temp.count(hyphen) == 1 and (temp[0] == hyphen or temp[len(temp) - 1] == hyphen or temp[temp.index(hyphen) + 1] in punctuation):
                continue
            else:
                count = 0
                for v in punctuation:
                    count += temp.count(v)

                if count > 1:
                    continue
                elif count == 1 and temp[len(temp) - 1] not in punctuation:
                    continue
                else:
                    valid += 1

        return valid
