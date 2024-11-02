class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedLst=sorted(nums)
        res=[]
        dic={}
        for j in range(len(sortedLst)):
            if sortedLst[j] not in dic:
                dic[sortedLst[j]]=j
        for n in nums:
            res.append(dic[n])
        return res
