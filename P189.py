class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=1
        while i<=k:
            nums.insert(0,nums.pop())
            i+=1       
