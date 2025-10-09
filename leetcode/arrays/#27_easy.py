'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
from typing import List
class Solution:
    #way 1:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[end] == val:
                end-=1
                continue
            if nums[start] == val:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
                continue
            start+=1
        print(nums)
        return end+1

    #way 2 and optimal code:
    def remove_element(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        while start <= end:
            if nums[start] == val:
                nums[start] = nums[end]
                end-=1
            else:
                start+=1
        return end+1