class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        i=0

        while i<l:
            print(nums)
            if nums[i]==val:
                nums.pop(i)
                l-=1
                i-=1
            i+=1
