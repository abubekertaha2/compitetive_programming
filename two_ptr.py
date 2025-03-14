# numbr=[0,4,0,1,3,0,3,0,6,7,0,7,9]
# hldr,skr=0,0
# while skr < len(numbr):
#     if numbr[skr] != 0:
#         numbr[hldr], numbr[skr] = numbr[skr] , numbr[hldr]
#         hldr+=1
#     skr+=1
# print(numbr)
#for-while combo
# a = [2,2,5,6]
# b = [3,4,6,8]
# C = []
# i=0
# for j in range(len(b)):
#     while i < len(a) and a[i] < b[j]:
#         i+=1
#     C.append(i)
# print(C)
a,b = map(int, input().split())
num1 =list (map(int, input().split()))
num2 =list (map(int, input().split()))
i=0
ans=[]
for j in range(b):
    while i < a and num1[i] < num2 [j]:
        i+=1
    ans.append(i)
print(*ans)