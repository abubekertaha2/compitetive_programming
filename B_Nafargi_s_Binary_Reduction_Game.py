n = int(input())
s = input()
stack =[]
for i in s:
    if stack and stack[-1] != i:
        stack.pop()
    else:
        stack.append(i)
print(len(stack))