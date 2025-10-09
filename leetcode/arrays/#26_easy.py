from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p0,p1 = 0,1
        while p1 < len(nums):
            if nums[p0] == nums[p1]:
                p1+=1
            elif nums[p0] < nums[p1]:
                p0+=1
                nums[p0] = nums[p1]
        return p0+1
            
            
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        p0 = 0
        for p1 in range(1, len(nums)):
            if nums[p1] != nums[p0]:
                p0 += 1
                nums[p0] = nums[p1]
        return p0 + 1