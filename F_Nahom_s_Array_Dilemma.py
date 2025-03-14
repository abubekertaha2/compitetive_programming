t = int(input())
for _ in range(t):
    n = int(input())
    a= list(map(int, input().split()))
    for i in range(1,n):
        if (a[i] > 0 and a[i-1] >0) or (a[i] <0 and a[i-1] < 0):
            print("NO")
            break
        else:
            if i == n-1:
                print("YES")