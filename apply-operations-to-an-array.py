class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
        for i in (nums):
            if i!=0:
                arr.append(i)
        new_list = arr.copy() 
        new_list.extend([0] * (len(nums) - len(arr)))
        return new_list
