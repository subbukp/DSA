'''
238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        This method does in in-place but uses division and kinda complex
        '''
        product = 1
        flag = 0
        for num in nums:
            if num!=0:
                product*=num
            elif num == 0:
                flag += 1
        for i, num in enumerate(nums):
            if flag > 0:
                if num == 0:
                    if flag == 1:
                        nums[i] = product
                    if flag >1:
                        nums[i] = 0
                elif num != 0:
                    nums[i] = 0
                continue
            nums[i] = int(product/num)
        return nums
    
    def product_exceptSelf(self, nums: List[int]) -> List[int]:
        '''
        This method consumes extra space but doesnt use any division and works on prefix and suffix thing
        '''
        product = [1]*len(nums)
        for i in range(1, len(nums)):
            product[i]=nums[i-1]*product[i-1]
        suffix=1
        for j in range(len(nums)-1,-1,-1):
            product[j]*=suffix
            suffix*=nums[j]
        return product
