class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        tmp = ""

        while columnNumber > 0:
            columnNumber -= 1
            tmp += chr(ord("A") + columnNumber % 26)
            columnNumber //= 26

        return tmp[::-1]