class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        new_strs=sorted(strs)
        length=min(len(new_strs[0]),len(new_strs[-1])) # new_strs[0]),new_strs[-1] contain maximum difference of the elemnet of stsrs after sorting
        for i in range(length):
            if new_strs[0][i]!=new_strs[-1][i]:
                return res
            res+=new_strs[0][i]
        return res
