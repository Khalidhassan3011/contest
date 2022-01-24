class Solution:

    def method1(self, address: str) -> str:
        defang: str = ""
        for l in address:
            if l == ".":
                defang += "[.]"
            else:
                defang += l

        return defang

    def method2(self, address: str) -> str:
        return address.replace(".", "[.]")

    def defangIPaddr(self, address: str) -> str:
        return self.method1(address)
