class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        maxi=max(arr)
        indx=arr.index(maxi)
        if len(arr)<3 or (indx==0 or indx==len(arr)-1) :
            return False
        for i in range(1,indx):
            if arr[i-1]>=arr[i]:
                return False
        for j in range(indx+1,len(arr)):
            if arr[j-1]<=arr[j]:
                return False
        return True
