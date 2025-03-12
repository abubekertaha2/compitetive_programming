n, m= map(int, input().split())
nums = list(map(int, input().split()))
Sum =0
l = 0
max_len = 0
for i in range(len(nums)):
    while Sum > m:
        Sum -= nums[l]
        l+=1
    max_len = max(max_len , i - l)
    Sum += nums[i]
print(max_len)