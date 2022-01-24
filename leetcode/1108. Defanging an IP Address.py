class Solution:

    def method1(self, address: str) -> str:
        pass

    # faster than 86.07% of Python3
    def method2(self, address: str) -> str:
        return address.replace(".", "[.]")

    def defangIPaddr(self, address: str) -> str:
        return self.method2(address)


s = Solution()
print(s.defangIPaddr("1.1.1.1"))
