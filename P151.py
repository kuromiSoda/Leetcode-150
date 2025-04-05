class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        x=s.split()
        return " ".join(x[::-1])
