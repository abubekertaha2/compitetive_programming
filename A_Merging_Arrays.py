n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split())) 
new_arr = []
i, j = 0, 0
while i < n and j < m:
    if arr1[i] < arr2[j]:
        new_arr.append(arr1[i])
        i += 1
    else:
        new_arr.append(arr2[j])
        j += 1
 
new_arr.extend(arr1[i:])
new_arr.extend(arr2[j:])
print(*new_arr)