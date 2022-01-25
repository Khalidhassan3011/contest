class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        only_num = [int(word) for word in s.split() if word.isdigit()]
        remove_dup = set(n for n in only_num if only_num.count(n) > 1)

        return False if len(remove_dup) > 0 else only_num == sorted(only_num)