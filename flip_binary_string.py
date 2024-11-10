"""class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n=len(flips)
        lst=[0]*n
        num_times=0
        for i in range(len(flips)):
            lst[flips[i]-1]=1
            if '0' in lst[:flips[i-1]]:
                continue
            else:
                num_times+=1
        return num_times"""

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0 
        num_times = 0  

        for i in range(len(flips)):
            max_flip = max(max_flip, flips[i])
            if max_flip == i + 1: 
                num_times += 1 

        return num_times
