'''
Remove Duplicates from Sorted Array II:

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p0 = 0
        count = 1
        for p1 in range(1, len(nums)):
            if nums[p0] == nums[p1]:
                count+=1
                if count == 2:
                    p0+=1
                    nums[p0]=nums[p1]
            elif nums[p0]!= nums[p1]:
                p0+=1
                nums[p0]=nums[p1]
                count=1
        return p0+1
    
    def remove_duplicates(self, nums: List[int]) -> int:
        k = 0  # next write position
        for x in nums:
            # allow at most 2 copies: write if we have <2 so far
            # or x differs from the element 2 slots back
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k
