n, m = map(int, input().split())
nums = list(map(int, input().split()))
Sum = 0
l = 0
min_len = float("inf")

for i in range(len(nums)):
    Sum += nums[i]  

    while Sum >= m:
        min_len = min(min_len, i - l + 1)  
        Sum -= nums[l]
        l += 1 
if min_len == float("inf"):
    print(-1)  
else:
    print(min_len)