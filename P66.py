class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = [str(i) for i in digits]
        d = str(int(''.join(d))+1)
        d = [int(i) for i in d]
        return d
