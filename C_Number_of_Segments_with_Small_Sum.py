n, m= map(int, input().split())
nums = list(map(int, input().split()))
Sum =0
l , count = 0, 0
#max_len = 0 
for i in range(len(nums)):
    Sum += nums[i]
    while Sum > m:
        Sum -= nums[l]
        l+=1
    count +=i - l + 1
print(count)
