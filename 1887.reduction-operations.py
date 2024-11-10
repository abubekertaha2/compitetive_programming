class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums=sorted(nums)
        num_set=set(nums)
        cnt=0
        for i in range(len(num_set)):
            cnt+=i
        return i
