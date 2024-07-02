class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        initial_max = -float('inf')
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = initial_max
            initial_max = max(initial_max,temp)
        arr[-1]=-1
        return arr
