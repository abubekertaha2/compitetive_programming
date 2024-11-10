class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n=max(costs)
        lst=[0]*(n+1)
        for num in costs:
            lst[num]+=1
        for j in range(1,len(lst)):
            lst[j]+=lst[j-1]
        sorted_lst=[0]*len(costs)
        for i in costs[::-1]:
            sorted_lst[lst[i]-1]=i
            lst[i]-=1
        res, cnt = coins, 0
        for cost in sorted_lst:
            if res >= cost:
                res -= cost
                cnt += 1
            else:
                break
        return cnt
