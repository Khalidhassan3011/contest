class Solution:

    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        date_sep = date.split()
        return f"{date_sep[2]}-{str(month.index(date_sep[1])+1).zfill(2)}-{date_sep[0][:-2].zfill(2)}"


s = Solution()
a = s.reformatDate(date="20th Oct 2052")
print(a)
print(a == "2052-10-20")
