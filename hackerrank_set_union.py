# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
engli_sub=list(map(int, input().split()))
m=int(input())
french_sub=list(map(int, input().split()))
print(len(set(engli_sub + french_sub)))
