def solve():
    n = int(input())
    a = input()
    b = input()

    diff = 0
    balance = 0
    for i in range(n - 1, -1, -1):
        if a[i] != b[i]:
            if balance == 0:
                diff ^= 1
            else:
                if diff == 1:
                    pass
                else:
                    pass
        if a[i] == '0':
            balance -= 1
        else:
            balance += 1

        if balance == 0:
            continue
        if diff == 1 and a[i] != b[i]:
            return "NO"
    
    if diff == 0:
        return "YES"
    else:
        return "NO"
    

t = int(input())
for _ in range(t):
    print(solve())