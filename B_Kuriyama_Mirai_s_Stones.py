import itertools
n = int(input())
arr = list(map(int, input().split()))
new_arr =sorted(arr)
cum_sum=[0]*(len(arr) + 1)
for i in range(len(arr)):
     cum_sum[i+1] = cum_sum[i] + arr[i]
cum_sum1=[0]*(len(arr) + 1)
for i in range(len(arr)):
     cum_sum1[i+1] = cum_sum1[i] + new_arr[i]
m = int(input())
for _ in range(m):
    ans = 0
    t,l,r = map(int, input().split())
    if t ==1:
        ans =cum_sum[r]-cum_sum[l-1]
    else:
        ans = cum_sum1[r]-cum_sum1[l-1]
    print(ans)
