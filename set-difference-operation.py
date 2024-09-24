n=int(input())
num=list(map(int, input().strip().split()))
m=int(input())
num2=list(map(int, input().strip().split()))
res=0
res+=sum(1 for i in num if i not in num2)
print(res)

# Enter your code here. Read input from STDIN. Print output to STDOUT
