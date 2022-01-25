class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        only_num = [int(word) for word in s.split() if word.isdigit()]
        remove_dup = set(n for n in only_num if only_num.count(n) > 1)

        return False if len(remove_dup) > 0 else only_num == sorted(only_num)


s = Solution()
print(s.areNumbersAscending(s="1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print(s.areNumbersAscending(s="hello world 5 x 5"))
print(s.areNumbersAscending(s="sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"))
