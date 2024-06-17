class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        res=0
        for i in range(n,2*n+1):
            if i%2==0 and i%n==0:
                res=i
                break
        return res
