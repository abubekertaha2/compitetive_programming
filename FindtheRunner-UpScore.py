if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    left = float('-inf')
    right=max(left, left)
    for i in arr:
        if i>right:
            left=right
            right=i
        elif i>left and i!=right:
            left=i
    print(left)
            
