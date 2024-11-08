class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        new_piles = sorted(piles)
        n = len(new_piles) // 3 
        res = 0
        r = len(new_piles) - 1 
        for i in range(n):
            res += new_piles[r - 1] 
            r -= 2 

        return res
