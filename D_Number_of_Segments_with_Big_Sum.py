n, m = map(int, input().split())
nums = list(map(int, input().split()))
length = len(nums)
Sum = 0
l = 0
count = 0

for i in range(len(nums)):
    Sum += nums[i]  

    while Sum >= m:
        count += length - i  
        Sum -= nums[l]
        l += 1
print(count) 
