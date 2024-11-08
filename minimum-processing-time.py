class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        result,i = 0,0
        for j in processorTime:
            current=0
            count=0
            while i<len(tasks) and count<4:
                current=max(current,j+tasks[i])
                i+=1
                count+=1
            result=max(result,current)
        return result
