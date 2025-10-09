'''
169. Majority Element:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Solution works on: Boyer-Moore Majority Voting Algorithm
-> https://www.geeksforgeeks.org/theory-of-computation/boyer-moore-majority-voting-algorithm/

It will pick first element as candidate and count+=1 whenever there is a same occurance of candidate
and if diff candidate occurs it will do count-=1
and if that candidate count is 0 new element will be candidate as its more thn half
'''
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate =nums[0]
        for i in nums:
            if candidate == i:
                count+=1
            elif count!=0 and candidate != i:
                count-=1
            elif count == 0:
                candidate = i
        return candidate
