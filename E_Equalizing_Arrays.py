def eval():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    if sum(a) != sum(b):
        return -1
    
    ans = 0
    l, r = 0, 0
    a1, b1 = 0, 0  
    while l < n or r < m:
        if a1 < b1:
            a1 += a[l]
            l += 1
        elif b1 < a1:
            b1 += b[r]
            r += 1
        else:
            ans += 1
            a1 += a[l]
            b1 += b[r]
            l += 1
            r += 1

    return ans

res = eval()
print(res)

     