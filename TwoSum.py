class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,j in enumerate(nums):
            dig=target-j
            if dig in dic:
                return [dic[dig],i]
            dic[j]=i
        return
        
