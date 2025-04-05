class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l=len(nums)
        n=list(set(nums))
        d={}
        for i in n:
            d[i]=nums.count(i)
        for i in d:
            if d[i]>(l//2):
                return i
