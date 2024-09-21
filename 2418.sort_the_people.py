class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peop=list(zip(names,heights))
        sorted_peop = sorted(peop, key=lambda x: x[1], reverse=True)
        return [name for name,_ in sorted_peop]
