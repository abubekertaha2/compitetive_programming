class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h_map={val:indx for indx, val in enumerate(arr2) }
        new_arr1=[]
        new_arr2=[]
        for i in arr1:
            if i in arr2:
                new_arr1.append(i)
            else:
                new_arr2.append(i)
        new_arr2.sort()
        new_arr1.sort(key=lambda x: h_map[x])
        return new_arr1 + new_arr2
