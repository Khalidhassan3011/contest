class Solution:

    # faster than 30.66% of Python3
    def method1(self, address: str) -> str:
        defang: str = ""
        for l in address:
            if l == ".":
                defang += "[.]"
            else:
                defang += l

        return defang

    # faster than 86.07% of Python3
    def method2(self, address: str) -> str:
        return address.replace(".", "[.]")

    def defangIPaddr(self, address: str) -> str:
        return self.method1(address)


s = Solution()
print(s.defangIPaddr("1.1.1.1"))
