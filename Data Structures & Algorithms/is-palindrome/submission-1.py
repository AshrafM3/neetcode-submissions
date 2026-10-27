class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ""
        b = ""

        for i in range(len(s)):
            if s[i].isalnum():
                b += s[i].lower()

        for i in range(len(s) - 1, -1, -1):
            if s[i].isalnum():
                a += s[i].lower()

        return a == b

                        