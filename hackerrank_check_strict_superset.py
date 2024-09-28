setA =set(map(int, input().split()))
is_setA_super=True
n=int(input())
for _ in range(n):
    new_set=set(map(int, input().split()))
    if not (setA) > new_set:
        is_setA_super=False
print(is_setA_super)
    
    
    
    
    
    
# Enter your code here. Read input from STDIN. Print output to STDOUT
