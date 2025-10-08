from typing import List
class arrays:
    def reverse(arr):
        left, right = 0, len(arr)-1
        while(left< right):
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
        return arr
    reverse([0,2,34,3,1,3,4,2,32])


    def shift_right(arr):
        if len(arr) ==1 or not arr:
            return arr
        tmp = arr[-1]
        for i in range(len(arr)-1,0,-1):
            arr[i] = arr[i-1]
        arr[0]=tmp
        return arr

    shift_right([1,2,3,4,5])

    def max_subarray_value(self, nums: List[int])->int:
        s = set()
        start=0
        max_val,current_val=0,0
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[start])
                start+=1
                
            s.add(nums[i])
            current_val = sum(s)
            max_val = max(max_val,current_val)
        return max_val
    
    def kadane(self,nums):
        max_sum = current_sum = nums[0]  # start with first number

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            #print("num: ",num)
            #print("current_sum: ",current_sum)
            max_sum = max(max_sum, current_sum)
            #print(max_sum)

        return max_sum
    def prefix_sum(self, arr:List[int])-> int:
        for i in range(len(arr),1,-1):
            sum=0
            for j in range(i):
                sum+=arr[j]
            arr[i-1]=sum
        return arr
    
    def build_prefix_sum(self,nums:List[int])->int:
        pre = [0]*len(nums)
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i]=nums[i]+pre[i-1]
        return pre
    
    #def sub_arr(self,nums:List[int],count) -> List[arr]:
    #    for i in range(len(nums)):
    #        pass

    def max_subarray(self, arr:List[int], n):
        window = sum(arr[:n])
        max_start_index=0
        max=window
        for i in range(len(arr)-n):
            window = window + arr[i+n] - arr[i]
            if window > max:
                max = window
                max_start_index = i+1
        return sum(arr[max_start_index:max_start_index+n])    
            
arr = arrays()
(arr.max_subarray_value([1,4,3,3,2,-4,-2]))
(arr.kadane([1,4,3,3,2,-4,-2]))
(arr.prefix_sum([1,2,3,4,5]))
#arr.sub_arr([1,2,3,12,4,2],6)
print(arr.max_subarray([1,2,3,12,4,2],3))