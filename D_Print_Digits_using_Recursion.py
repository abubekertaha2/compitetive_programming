t = int(input())
for _ in range(t):
    num =int(input())
    def recursion(num):
            if num < 10:
                print(num, end=" ")
                return 
            else:
                recursion(num//10)
                print(num%10, end=" ")
    recursion(num)
    print()
