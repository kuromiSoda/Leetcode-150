class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x.lower() for x in s if x.isalnum()]
        if s==s[::-1]:
            return True
        return False
