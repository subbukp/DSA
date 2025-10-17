'''
42. Trapping Rain Water:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = len(height)-1
        left_max, right_max = 0,0
        water = 0
        while p1 < p2:
            if height[p1] < height[p2]:
                if height[p1] > left_max:
                    left_max = height[p1]
                else:
                    water+=left_max-height[p1]
                p1+=1
            else:
                if height[p2] > right_max:
                    right_max=height[p2]
                else:
                    water+=right_max-height[p2]
                p2-=1
        return water


        