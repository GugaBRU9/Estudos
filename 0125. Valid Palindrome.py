class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = ''
        for c in s:
            if c.isalpha():
                txt += c.lower()

        txt = ''.join(txt.split())
        print(txt)
        return txt == txt[::-1]

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))