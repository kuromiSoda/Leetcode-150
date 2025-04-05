class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0 and x<=9:
            return True
        elif x<0:
            return False
        else:
            return str(x)==str(x)[::-1]
