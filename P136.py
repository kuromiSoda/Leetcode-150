class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        if len(nums)==1:
            return nums[0]
        else:
            d=Counter(nums)
            l = [key for key, value in d.items() if value == 1]
            return l[0]
