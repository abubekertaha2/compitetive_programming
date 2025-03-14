t = int (input())
for i in range(t):
    a,b,c = map(int, input().split())
    if a ==b and b == c and c==a:
        print(1,1,1)
    else:
        ans = max(a,b,c)
        if a== ans and b==ans:
            print(1,1,ans-c +1)
        elif a== ans and c==ans:
            print(1,ans-b +1,1)
        elif b== ans and c==ans:
            print(ans-a+1,1,1)
        else:
            if a == ans and b != ans and c!=ans:
                print(0,ans -b +1, ans-c +1)
            elif a != ans and b == ans and c!=ans:
                print(ans -a +1, 0 , ans-c +1)
            elif a != ans and b != ans and c==ans:
                print(ans-a +1, ans-b+1, 0)
