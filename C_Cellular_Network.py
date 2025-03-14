#Brute Force
# n , m= map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# res = 0
# for i in range(len(a)):
#     ans =float("inf")
#     for j in range(len(b)):
#         ans = min(abs(a[i]-b[j]),ans)
#     res = max(ans, res)
# print(res)
# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i, j = 0, 0
res = 0

while i < n:
    while j < m - 1 and abs(a[i] - b[j]) >= abs(a[i] - b[j + 1]):
        j += 1
    min_distance = abs(a[i] - b[j])
    res = max(res, min_distance)
    
    i += 1

print(res)

