from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst1=Counter(nums1)
        lst2=Counter(nums2)
        return list((lst1 & lst2).elements())
