class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x.lower() for x in s if x.isalnum()]
        if s==s[::-1]:
            return True
        return False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x.lower() for x in s if x.isalnum()]
        l,r=0,len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
